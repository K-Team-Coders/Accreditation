import os
import time
import json
import docx
import nltk
import shutil
import psycopg2
import numpy as np 
import pandas as pd
from pathlib import Path
from loguru import logger  
from pymystem3 import Mystem
from string import punctuation
from dotenv import load_dotenv
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, Request, UploadFile, Response
from fastapi.responses import JSONResponse
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

gost_compare = 0
gost_compare_path = Path().cwd().joinpath("gosts").joinpath("gosts_compare.json")
with open(gost_compare, 'rb') as f:
    gost_compare = json.load(f)

our_data=pd.read_csv(Path.cwd().joinpath("data_classes.csv"))
mystem = Mystem() 
russian_stopwords = stopwords.words("russian")
nltk.download("stopwords")

def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords\
              and token != " " \
              and token.strip() not in punctuation]
    
    text = " ".join(tokens)
    
    return text

def get_predictions(input_strings,target_strings,similarity_threshold=0.5):
    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2))

# Преобразуем тексты в матрицу TF-IDF
    tfidf_matrix_input = tfidf_vectorizer.fit_transform(input_strings)
    tfidf_matrix_target = tfidf_vectorizer.transform(target_strings)

    # Вычисляем косинусное сходство между входными и целевыми строками
    cosine_similarities = linear_kernel(tfidf_matrix_target, tfidf_matrix_input)

    # Находим индексы строк с сходством выше порога
    most_similar_indices = np.argwhere(cosine_similarities > similarity_threshold)

# Выводим только строки, у которых сходство больше 70%
    list_values={}
    for i, j in most_similar_indices:
        input_str = input_strings[j]
        target_str = target_strings[i]
        similarity = cosine_similarities[i, j]
        list_values[input_str]=similarity
        logger.debug(f"Целевая строка: {target_str}")
        logger.debug(f"Наиболее подходящая строка: {input_str}")
        logger.debug(f"Сходство (TF-IDF): {similarity}")
        logger.debug("---------")
    return set(list_values)

PRODUCTION = False

DBenv = Path().cwd().parent.joinpath("DB.env")
load_dotenv(DBenv, override=True)

conn = 0
cur = 0

logger.debug("Waiting for DB service Up...")
time.sleep(5)

try:     
    HOST = None
    DBNAME = None
    PASSWORD = None

    if PRODUCTION:
        HOST=os.environ.get("DB_HOST")  
        DBNAME=os.environ.get("POSTGRES_DB")
        USER=os.environ.get("POSTGRES_USER")
        PASSWORD=os.environ.get("POSTGRES_PASSWORD")
    else:
        HOST=os.environ.get("DB_LOCAL")
        DBNAME=os.environ.get("LOCAL_DB")
        USER=os.environ.get("LOCAL_USER")
        PASSWORD=os.environ.get("LOCAL_PASSWORD")
    
    PORT=os.environ.get("PORT")

    logger.success(('Docker DB connection started \n', HOST, PORT, DBNAME, USER, PASSWORD, ' - env variables!'))

    conn = psycopg2.connect(
        dbname=DBNAME, 
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        port=PORT)

    cur = conn.cursor()

    if PRODUCTION:
        logger.success('Docker DB connected!')
    else:
        logger.success('Local DB connected!')

except Exception as e:
    logger.error(f'Database connect failed \n {e}!')

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/allGosts")
async def getAllGosts():
    cur.execute("SELECT * FROM gosts")
    data = cur.fetchall()
    
    gosts = []
    for index, subdata in enumerate(data):
        # logger.debug(subdata[1]) # name
        # logger.debug(subdata[2]) # equip
        gosts.append(subdata[1].replace('.docx', ''))

    return JSONResponse(content={"docs": gosts}, status_code=200)

@app.post("/get_pred")
async def upload_folder_get_pred(request: Request,  file: UploadFile = File(...)):
    # Get the folder name from the request parameter
    path_to_save=Path.cwd().joinpath('download').joinpath(file.filename)
    with open(path_to_save, "wb") as dest_file:
        shutil.copyfileobj(file.file, dest_file)

    # Work on it
    doc = docx.Document(Path(path_to_save))
    full_text=[]
    for elem in doc.paragraphs:
        full_text.append(elem.text)

    prediction=get_predictions(our_data.text.values.tolist(),full_text)

    return {"prediction": prediction}

@app.post("/check_dataset")
async def upload_dataset(request: Request, file: UploadFile = File(...)):
    path_to_save = Path.cwd().joinpath('datacheck').joinpath(file.filename)

    with open(path_to_save, "wb") as dest_file:
        shutil.copyfileobj(file.file, dest_file)

    logger.debug(gost_compare)
    # Open via pandas
    # df = pd.read_csv(path_to_save)
    # for row in df.iterrows():
    #     index = row[1][0] # index
    #     gost = row[1][1] # GOSTS
    #     group = row[1][2] # Group
    #     name = row[1][3] # Naming
    #     tnved = row[1][4] # TN VED
    #     equip = row[1][5] # Apparats

    return Response(status_code=200)

@app.post("/train")
async def train_upload_dataset(request: Request, file: UploadFile = File(...)):
    database = Path.cwd().joinpath('download')
    path_to_save = database.joinpath(file.filename)

    # saved file
    with open(path_to_save, "wb") as dest_file:
        shutil.copyfileobj(file.file, dest_file)

    # clear all database
    cur.execute('TRUNCATE gosts CASCADE;')
    conn.commit()

    # go check all files and wite to database!
    for path in database.iterdir():
        doc = docx.Document(Path(path))
        full_text=[]
        for elem in doc.paragraphs:
            full_text.append(elem.text)

        prediction=get_predictions(our_data.text.values.tolist(),full_text)
        
        result = ""
        for subresult in prediction:
            result += str(subresult) + " ;; "

        logger.debug(result)

        try:
            cur.execute("INSERT INTO gosts (name, equip) VALUES (%s, %s) ON CONFLICT DO NOTHING;", (path.name, result))
            conn.commit()
            logger.success(f'Added {path.name}')
        except Exception as e:
            conn.rollback()
            logger.error(e)

    return Response(status_code=200)

