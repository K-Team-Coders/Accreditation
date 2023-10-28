<template>
  <div
    class="fixed xl:pt-3 inset-0 z-10 bg-black bg-opacity-75 focus:outline-none"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div class="bg-gray-200 w-[95%] mx-auto xl:my-2">
      <div class="flex justify-end m-2">
        <ModalWindowButtonClose @click="close" />
      </div>
      <div class="">
        <div class="flex gap-2 justify-center">
          <p class="text-center pb-4 font-bold text-2xl">ID: {{ id }}</p>
          <p class="text-center pb-4 font-bold text-2xl">Название группы</p>
        </div>
        <div
          class="flex transition justify-between h-full py-1 pb-4 px-4 ml-2 mr-4 leading-normal"
        >
          <p
            class="mb-1 pb-2 px-1 text-2xl w-1/2 h-[700px] overflow-y-scroll font-roboto font-bold text-gray-800 border-r-2 border-black"
          >
            Пользовательское оборудование:
            <span class="font-normal text-base">
              <li class="" v-for="(item, index) in 12" :key="index">
                Я сосу леденец огрымный он такой вкусный я не могу поогите мне я
                хочу пойти спать в коробку быстрее голова болит ааааа преза еще
                утром надо сделать
              </li>
            </span>
          </p>
          <p
            class="mb-1 pl-6 text-2xl w-1/2 h-[700px] overflow-y-scroll font-roboto font-bold text-black"
          >
            Оборудование по стандартам ГОСТ:
            <span class="font-normal text-base">
              <li class="" v-for="(item, index) in 12" :key="index">
                Я сосу леденец огрымный он такой вкусный я не могу поогите мне я
                хочу пойти спать в коробку быстрее голова болит ааааа преза еще
                утром надо сделать
              </li></span
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ModalWindowButtonClose from "./ModalWindowButtonClose.vue";

export default {
  components: {
    ModalWindowButtonClose,
  },
  props: {
    row_data: Array
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
  mounted() {
    this.$el.focus();
  },
  emits: ["close"],
};
</script>
