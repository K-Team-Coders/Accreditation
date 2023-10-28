<template>
  <div class="py-3">
    <form class="mb-2 px-4 xl:px-0">
      <label
        for="default-search"
        class="mb-2 text-sm font-medium text-gray-900 sr-only"
        >Искать</label
      >
      <div class="flex">
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
          class="text-white bg-[#e40046] hover:bg-red-700 duration-300 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm xl:px-4 xl:py-2 px-2 py-1"
        >
          Загрузить
        </button>
      </div>
    </form>
    <p class="px-4 font-bold">Обработанные руководящие документы. Всего: {{ docks.length }}</p>
    <div
      class="text-lg px-4 xl:px-0 h-96 grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-2 py-4 text-gray-800 font-roboto font-medium text-left overflow-y-auto"
    >
      <div
        v-for="doc in docks" :key="doc"
        class="cursor-pointer shadow-md hover:text-[#e40046] text px-4 py-2 duration-300 bg-gray-300 rounded-lg"
      >
        {{doc}}
        <p class="text-gray-600 text-right duration-300 hover:underline">
          скачать
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data(){
    return {
      docks: []
    }
  },
  mounted(){
    axios.get(`http://${process.env.VUE_APP_USER_IP_WITH_PORT}/allGosts/`)
    .then(response => (this.docks = response.data.docs,
    console.log(this.docks)))
    
  }
}
</script>