<template>
  <div
    class="bg-gray-50 2xl:max-w-4xl xl:max-w-3xl lg:max-w-2xl md:max-w-2xl sm:max-w-xl max-w-[320px] p-4 w-full px-4 py-3 rounded-lg shadow-md"
  >
    <form>
      <div class="flex items-center py-2">
        <input
          class="w-full text-sm text-gray-700 border-[0.5px] py-1 px-2 border-[#e40046] rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
          aria-describedby="file_input_help"
          id="files"
          ref="files"
          type="file"
        />
        <p class="mt-2.5 ml-2 text-sm text-gray-500" id="file_input_help">
          .xlsx
        </p>
      </div>
      <div class="flex justify-end pt-2">
        <button
          type="submit"
          class="text-whitesmoke bg-[#e40046] hover:bg-[#ce134b] focus:ring-4 focus:outline-none focus:ring-[#ce134b] font-semibold rounded-lg text-sm w-full sm:w-auto px-4 py-2.5 text-center mt-2"
        >
          Проверить файл
        </button>
      </div>
    </form>
  </div>
</template>
