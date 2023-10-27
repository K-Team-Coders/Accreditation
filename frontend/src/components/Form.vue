<template>
  <div
    class="bg-gray-50 2xl:max-w-4xl xl:max-w-3xl lg:max-w-2xl md:max-w-2xl sm:max-w-xl max-w-[320px] p-4 w-full px-4 py-3 rounded-lg shadow-xl"
  >
    <form class="">
      <div class="flex items-center border-b border-[#e40046] py-2">
        <input
          v-model="text"
          class="appearance-none bg-transparent border-none w-full text-gray-700 font-semibold mr-3 py-1 px-2 leading-tight focus:outline-none"
          type="text"
          placeholder="Напишите номер продукта"
          aria-label="Full name"
        />
        <button
          class="flex-shrink-0 bg-[#e40046] hover:bg-[#e40046] border-[#e40046] hover:border-[#e40046] text-sm border-4 text-whitesmoke font-semibold py-1 px-4 rounded-lg"
          type="button"
        >
          Отправить
        </button>
      </div>
    </form>
  </div>
</template>
<script>
export default {};
</script>
