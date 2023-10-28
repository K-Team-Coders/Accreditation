<template>
  <div
    class="fixed xl:pt-3 inset-0 z-10 bg-black bg-opacity-75 focus:outline-none"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div class="bg-gray-200 w-[95%] mx-auto xl:my-2 ">
      <div class="flex justify-end p-2">
        <ModalWindowButtonClose @click="close" />
      </div>
      <div class="">
        <div
          class="flex transition justify-between h-full py-1 pb-4 px-4 ml-2 mr-4 leading-normal"
        >
          <p
            class="mb-1 pb-2 text-2xl w-1/2 h-[700px] overflow-y-scroll font-roboto font-bold text-gray-800 border-r-2 border-black"
          >
            Пользовательское оборудование:
            <span class="font-normal text-base">
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Cupiditate magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium. Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.Lorem
              ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
              magni, mollitia iure ullam, corporis adipisci quibusdam
              repellendus aspernatur commodi consequuntur id labore nostrum
              nulla eligendi temporibus neque doloribus ad praesentium.
            </span>
          </p>
          <p
            class="mb-1 pl-3 text-2xl py-2 w-1/2 h-[700px] overflow-y-scroll font-roboto font-bold text-black"
          >
            Оборудование по стандартам ГОСТ:
            <span class="font-normal text-lg">
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ad,
              aperiam. Unde est ab assumenda consequuntur dolor ex eos nulla,
              voluptas asperiores ducimus nemo magnam earum inventore modi
              molestiae non recusandae!</span
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
