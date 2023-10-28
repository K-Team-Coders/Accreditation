import os
import time
import json
import docx

import shutil
import psycopg2
from pathlib import Path
from loguru import logger  
from dotenv import load_dotenv

import pandas as pd
import numpy as np 

import nltk
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, Request, UploadFile, Response
from fastapi.responses import JSONResponse

from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity

nltk.download('stopwords')

standars_info_path = Path().cwd().joinpath('gosts').joinpath('standarts.csv')
standars_info = pd.read_csv(standars_info_path)

# Файл для сопоставления ГОСТОВ и Групп\Подгрупп продукции
gost_compare = 0
gost_compare_path = Path().cwd().joinpath("gosts").joinpath("gosts_compare.json")
with open(gost_compare_path, 'rb') as f:
    gost_compare = json.load(f)
gost_compare = gost_compare["data"]

our_data=pd.read_csv(Path.cwd().joinpath("data_classes.csv"), encoding="utf-8", delimiter='"')
mystem = Mystem() 
russian_stopwords = stopwords.words("russian")
nltk.download("stopwords")

def compute_similarity_precentages(sentences1, sentences2):
    all_sentences = sentences1 + sentences2
    tfidf_vectorizer = CountVectorizer(ngram_range=(1, 2))
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_sentences)
    tfidf_matrix_sentences1 = tfidf_matrix[:len(sentences1)]
    tfidf_matrix_sentences2 = tfidf_matrix[len(sentences1):]
    similarity_matrix = cosine_similarity(tfidf_matrix_sentences1, tfidf_matrix_sentences2)
    
    similarity_percentages = [np.round(similarity * 100, 2) for similarity in similarity_matrix]

    return similarity_percentages 

def calculate_similarity_score(list1, list2):
    tfidf_vectorizer = CountVectorizer(ngram_range=(1, 2))

    tfidf_matrix_input = tfidf_vectorizer.fit_transform(list1)
    tfidf_matrix_target = tfidf_vectorizer.transform(list2)

    cosine_similarities = linear_kernel(tfidf_matrix_target, tfidf_matrix_input)

    return(np.mean(cosine_similarities))

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
        # logger.debug(f"Целевая строка: {target_str}")
        # logger.debug(f"Наиболее подходящая строка: {input_str}")
        # logger.debug(f"Сходство (TF-IDF): {similarity}")
        # logger.debug("---------")
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
    
    cur.execute("SELECT * FROM gosts;")
    data = cur.fetchall()

    total_gost_data = []
    for index, subdata in enumerate(data):
        # logger.debug(subdata[0]) # id
        # logger.debug(subdata[1]) # name
        # logger.debug(subdata[2]) # equip

        total_gost_data.append({
            "name" : subdata[1],
            "equip": subdata[2]
        })

    result = []

    # Open via pandas
    df = pd.read_csv(path_to_save)
    for row in df[:5].iterrows():
        index = row[1][0] # index
        gost = row[1][1] # GOSTS
        group = row[1][2] # Group
        name = row[1][3] # Naming
        tnved = row[1][4] # TN VED
        equip = row[1][5] # Apparats

        uppergroup_on_current_group = []

        # try to find in uppergroups
        for uppergroup in gost_compare:
            key = list(uppergroup.keys())[0]
            values = list(uppergroup.values())[0]

            if group in values:
                uppergroup_on_current_group.append(key)

        # try to find gost on uppergroups 
        uppergroup_gosts = [] 
        for subgroup in uppergroup_on_current_group:
            subgroup_gosts = standars_info[standars_info["Группа продукции"] == subgroup]["Обозначение и наименование стандарта"].to_list()
            uppergroup_gosts.extend(subgroup_gosts)
        uppergroup_gosts = list(set(uppergroup_gosts))

        # check with our table && compare search result to validate equipment
        find_gosts = []
        find_equipment = []

        # if find groups
        if uppergroup_gosts:
            for subdata in total_gost_data:
                if subdata["name"].replace(' ', '').replace('"', '').replace("'", '').replace('\xa0', '') in [x.replace(' ', '').replace('"', '').replace("'", '').replace('\xa0', '') for x in uppergroup_gosts]:
                    find_gosts.append(subdata["name"].replace('\xa0', ' '))
                    find_equipment.extend(subdata["equip"].split(';;'))
        
        # Метрики !

        # Сумма по элементам
        # Обородувание из ГОСТА -- list(prediction)
        # Оборудование из Датасета -- [item for item in item['Техническое оборудование'].split(";") ]
        # Вернет лист эталонных с пользовательскими чем больше, тем чаще повторяется
        similarity_percentages = compute_similarity_precentages(find_equipment, equip.split(';'))
        similarity_percentages_len = len(similarity_percentages)
        similarity_percentages = sum([x / similarity_percentages_len for x in similarity_percentages]) 
        
        # Обший процент
        similarity_score = calculate_similarity_score(find_equipment, equip.split(';'))
                
        result.append(
            {
                "id": index,
                "docs": find_gosts,
                "group": group,
                "name": name,
                "tnved": tnved,
                "equipment_find_len": len(find_equipment),
                "equipment_find": find_equipment,
                "equipment_user": equip,
                "equipment_user_len": len(equip),
                "similarity_score": similarity_score
            }
        )
    # Прислать ему колонки и проверенный датасет
    return JSONResponse(status_code=200, content={"data": result})

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

        try:
            cur.execute("INSERT INTO gosts (name, equip) VALUES (%s, %s) ON CONFLICT DO NOTHING;", (str(path.name).replace('.docx', ''), result))
            conn.commit()
            logger.success(f'Added {path.name}')
        except Exception as e:
            conn.rollback()
            logger.error(e)

    return Response(status_code=200)

