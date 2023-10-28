<template>
  <div class="rounded-lg pt-6">
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg rounded-lg">
      <table class="w-full text-xs text-gray-500 table-auto text-center">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 font-bold">
          <tr>
            <th scope="col" class="px-6 py-3 cursor-pointer hover:text-[#e40046]">ID</th>
            <th scope="col" class="px-6 py-3 cursor-pointer hover:text-[#e40046]">Обозначение стандарта</th>
            <th scope="col" class="px-6 py-3 cursor-pointer hover:text-[#e40046]">Группа продукции</th>
            <th scope="col" class="px-6 py-3 cursor-pointer hover:text-[#e40046]">Наименование продукции</th>
            <th scope="col" class="px-6 py-3 cursor-pointer hover:text-[#e40046]">Коды ОКПД 2 / ТН ВЭД ЕАЭС</th>
            <th scope="col" class="px-6 py-3 cursor-pointer hover:text-[#e40046]">Техническое оборудование</th>
            <th scope="col" class="px-6 py-3 cursor-pointer hover:text-[#e40046]">Оборудование по госту</th>
            <th scope="col" class="px-6 py-3 cursor-pointer hover:text-[#e40046]">% соответствия</th>
          </tr>
        </thead>
        <tbody class="font-semibold">
          <tr
            v-for="el in 4"
            class="bg-white border-b hover:bg-gray-50"
          >
            <th
              scope="row"
              class="px-6 py-4 max-w-lg font-medium text-gray-900 whitespace-nowrap truncate"
            >
              {{ el }}
            </th>
            <td class="px-6 py-4">{{ el }}</td>
            <td class="px-6 py-4">{{ el }}</td>
            <td class="px-6 py-4">Ключевого слова нет</td>
            <td class="px-6 py-4">{{ el }}</td>
            <td class="px-6 py-4">{{ el }}</td>
            <td class="px-6 py-4">{{ el }}</td>
            <td class="px-6 py-4">{{ el }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    table_data: Array,
  },
  data() {
    return {};
  },
};
</script>
