<template>
  <div class="bg-[#b2a49b] h-44 rounded-xl shadow-xl flex items-center">
    <div class="">
      <BaseIcon :name="name" class="text-[whitesmoke] ml-6 w-32" />
    </div>
    <p
      class="mx-4 my-4 text-whitesmoke font-roboto xl:text-xl text-sm font-semibold text-left"
    >
      {{ text }}
    </p>
  </div>
</template>
<script>
import BaseIcon from "./BaseIcon.vue";
export default {
  components: { BaseIcon },
  props: ["name", "text"],
};
</script>