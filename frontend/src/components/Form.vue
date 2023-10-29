<template>
  <div class="flex flex-col justify-center xl:items-center px-4 xl:px-0">
    <div
      class="bg-gray-50 w-full px-4 py-3 rounded-lg shadow-md"
    >
      <form class="">
        <div class="flex items-center border-b border-[#e40046] py-2">
          <input
            v-model="text"
            class="appearance-none bg-transparent border-none w-full text-gray-700 font-semibold mr-3 xl:py-1 px-2 leading-tight focus:outline-none"
            type="text"
            placeholder="Введите наименование продукта"
            aria-label="Full name"
          />
          <button
            @click="submit_text()"
            type="submit"
            class="text-whitesmoke bg-[#e40046] hover:bg-[#ce134b] focus:ring-4 focus:outline-none focus:ring-[#ce134b] font-semibold rounded-lg text-sm w-full sm:w-auto px-4 py-2.5 text-center mt-2"
          >
            Отправить
          </button>
        </div>
      </form>
    </div>
    <div class="grid xl:grid-cols-3 lg:grid-cols-3 sm:grid-cols-2 grod-cols-1 gap-2 mt-10 mb-4">
      <Cards name="book" :text="pred_data.find_gosts" title="ГОСТ: " />
      <Cards name="tech" :text="pred_data.find_equipment" title="Оборудование: " />
      <Cards name="list" :text="pred_data.group" title="Группа продукции: " />
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Cards from "./Cards.vue";
import DownloadButtonGost from "./DownloadButtonGost.vue";
export default {
  components: { Cards, DownloadButtonGost },
  data() {
    return {
      text: "",
      pred_data: [],
    };
  },
  methods: {
   submit_text(){
    axios
        .post(
          `http://${process.env.VUE_APP_USER_IP_WITH_PORT}/predict?name=${this.text}`)
          .then(response => (this.pred_data = response.data,
          console.log(this.pred_data)))
   }
  },
};
</script>
