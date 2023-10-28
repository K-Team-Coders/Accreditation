<template>
  <div class="py-3">
    <form class="">
      <label
        for="default-search"
        class="mb-2 text-sm font-medium text-gray-900 sr-only"
        >Искать</label
      >
      <div class="relative">
        <input
          type="search"
          id="default-search"
          class="block w-full p-3 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-red-500 focus:border-red-500"
          placeholder="Введите что-нибудь"
          required
        />
        <button
          type="submit"
          class="text-white absolute right-3 bottom-2 bg-[#e40046] hover:bg-red-700 duration-300 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-4 py-2"
        >
          Искать
        </button>
      </div>
    </form>
    <div
      class="text-lg h-96 grid grid-cols-3 gap-2 py-4 text-gray-800 font-roboto font-bold text-left overflow-y-auto"
    >
      <div
        v-for="i in 20"
        class="cursor-pointer shadow-md hover:text-[#e40046] text px-4 py-2 duration-300 bg-gray-300 rounded-lg"
      >
        ГОСТ 12372 - Я ХОЧУ ЕСТЬ ПРОД ЖРА asdasdasdqwwe asjdhakj gdksab kdags
        dgaksjd nk dgqwyg sabdjb a jshdbkuygk
        <p class="text-gray-600 text-right duration-300 hover:underline ">скачать</p>
      </div>
    </div>
  </div>
</template>
