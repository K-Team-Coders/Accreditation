<template>
  <div class="flex flex-col justify-center xl:items-center px-4 xl:px-0">
    <div
      class="bg-gray-50 w-full px-4 py-3 rounded-lg shadow-md"
    >
      <form class="">
        <div class="flex items-center border-b border-[#e40046] py-2">
          <input
            v-model="text"
            @input="text_processing()"
            class="appearance-none bg-transparent border-none w-full text-gray-700 font-semibold mr-3 xl:py-1 px-2 leading-tight focus:outline-none"
            type="text"
            placeholder="Введите наименование продукта"
            aria-label="Full name"
          />
        </div>
      </form>
    </div>
    <div class="grid xl:grid-cols-4 lg:grid-cols-4 sm:grid-cols-2 grod-cols-1 gap-2 mt-10 mb-4">
      <Cards name="book" text="12367123" title="ГОСТ: " />
      <Cards name="code" text="17462935684123123123123123123123123фвфыпвгфнпвлфыивплфыгивлфыилывилфыивго 87" title="ТН ВЕД: " />
      <Cards name="tech" text="Текст" title="Оборудование: " />
      <Cards name="list" text="Текст" title="Группа продукции: " />
    </div>
    <div class="flex justify-center pb-10">
      <DownloadButtonGost />
    </div>
  </div>
</template>
<script>
import axios from "axios";
import debounce from "lodash/debounce";
import Cards from "./Cards.vue";
import DownloadButtonGost from "./DownloadButtonGost.vue";
export default {
  components: { Cards, DownloadButtonGost },
  data() {
    return {
      text: "",
      isTyping: false,
      textisProcessing: false,
      isError: false,
    };
  },
  methods: {
    startTyping() {
      this.isTyping = true;
      this.debounceStopTyping();
    },
    textChange() {},
    debounceStopTyping: debounce(function () {
      this.isTyping = false;
    }, 500),
    text_processing() {
      this.isError = false;
      this.isTyping = true;
      this.debounceStopTyping();
      setTimeout(() => {
        if (this.isTyping == false) {
          (this.textisProcessing = true),
            axios
              .post(`http://${process.env.VUE_APP_USER_IP_WITH_PORT}/answer/`, {
                usertext: this.text,
              })
              .then((response) => {
                this.tone = response.data;
                this.textisProcessing = false;
              })
              .catch(function () {
                console.log("Ошибка в обработке");
                this.textisProcessing = false;
                this.isError = true;
              });
          this.textisProcessing = false;
        } else {
          console.log("Ошибка ");
          this.textisProcessing = false;
          this.isError = true;
        }
      }, 600);
    },
  },
};
</script>
