<template>
  <div class="bg-[#b2a49b] h-44 rounded-xl shadow-md flex items-center hover:scale-105 duration-300 cursor-pointer">
    <div class="">
      <BaseIcon :name="name" class="text-[whitesmoke] ml-6 w-32" />
    </div>
    <div
      class="mx-4 my-4 text-whitesmoke font-roboto xl:text-xl text-sm font-semibold text-left items-end"
    >
      <span class="text-[#e40046] text-start text-2xl">{{ title }}</span>
      <span class="text-whitesmoke text-2xl ml-1">{{ text }}</span>
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
