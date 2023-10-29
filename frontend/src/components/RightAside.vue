<template>
 <div>
    <p class="px-4 font-bold">Обработанные руководящие документы. Всего: {{ docks.length }}</p>
    <div
      class="text-lg px-4 xl:px-0 h-96 grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-2 py-4 text-gray-800 font-roboto font-medium text-left overflow-y-auto"
    >
      <div
        v-for="doc in docks" :key="doc"
        class="cursor-pointer shadow-md hover:text-[#e40046] text px-4 py-2 duration-300 bg-gray-300 rounded-lg"
      >
        {{doc}}
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