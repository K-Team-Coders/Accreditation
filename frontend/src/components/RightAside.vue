<template>
  <div class="py-3">
    Обработанные файлы
    <form>
      <div class="flex items-center py-2">
        <input
        v-on:change="handleFilesUpload()"
          class="w-full text-sm text-gray-700 border-[0.5px] py-1 px-2 border-[#e40046] rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
          aria-describedby="file_input_help"
          id="files"
          ref="files"
          type="file"
        />
        <p class="mt-2.5 ml-2 text-sm text-gray-500" id="file_input_help">
          .docx
        </p>
      </div>
      <div class="flex justify-end pt-2">
        <button
        @click="submitFiles()" 
          type="submit"
          class="text-whitesmoke bg-[#e40046] hover:bg-[#ce134b] focus:ring-4 focus:outline-none focus:ring-[#ce134b] font-semibold rounded-lg text-sm w-full sm:w-auto px-4 py-2.5 text-center mt-2"
        >
          Загрузить
        </button>
      </div>
    </form>    Обработанные руководящие документы
    <div
      class="text-lg h-96 grid grid-cols-3 gap-2 py-4 text-gray-800 font-roboto font-medium text-left overflow-y-auto"
    >
   
      <div
        v-for="i in 20"
        class="cursor-pointer shadow-md hover:text-[#e40046] text px-4 py-2 duration-300 bg-gray-300 rounded-lg"
      >
      ГОСТ 126-79 Галоши резиновые клееные. Технические условия
        <p class="text-gray-600 text-right duration-300 hover:underline ">скачать</p>
      </div>
    </div>
  </div>
</template>
