<template>
  <div
    class="bg-[#b2a49b] xl:h-auto 2xl:w-full rounded-xl shadow-md flex items-center hover:scale-105 hover:shadow-2xl duration-300 cursor-pointer flex-col py-4 xl:pt-0"
  >
    <div class="flex">
      <BaseIcon :name="name" class="text-whitesmoke w-20" />
    </div>
    <div class="mx-4 pt-2 text-whitesmoke text-base font-semibold">
      <span class="text-[#e40046] text-start font-bold 2xl:text-2xl">{{
        title
      }}</span>
      <span class="text-whitesmoke xl:ml-1 2xl:text-2xl font-roboto break-all">{{
        text
      }}</span>
    </div>
  </div>
</template>
<script>
import BaseIcon from "./BaseIcon.vue";
export default {
  components: { BaseIcon },
  props: ["name", "text", "title"],
};
</script>
