<template>
  <div class="rounded-lg pt-6">
    <p class="text-center pb-4 font-bold text-xl">
      Выберите строчку для детального просмотра списков оборудований
    </p>
    <div
      class="shadow-md sm:rounded-lg rounded-lg overflow-x-auto h-[500px] xl:max-w-7xl lg:max-w-4xl md:max-w-3xl sm:max-w-2xl mx-auto max-w-[300px]"
    >
      <table class="w-full text-xs text-gray-500 table-auto text-center">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 font-bold">
          <tr>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-[#e40046]"
            >
              ID
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-[#e40046]"
            >
              Обозначение стандарта
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-[#e40046]"
            >
              Группа продукции
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-[#e40046]"
            >
              Наименование продукции
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-[#e40046]"
            >
              Коды ОКПД 2 / ТН ВЭД ЕАЭС
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-[#e40046]"
            >
              Оборудование пользователя
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-[#e40046]"
            >
              Оборудование по госту
            </th>
            <th
              scope="col"
              class="px-6 py-3 cursor-pointer hover:text-[#e40046]"
            >
              % соответствия
            </th>
          </tr>
        </thead>
        <tbody class="font-semibold ">
          <tr
            @click="isModalOpen = true"
            v-for="el in table_data" :key="el.key"
            class="bg-white border-b hover:bg-gray-50 cursor-pointer hover:text-red-600"
          >
            <th
              scope="row"
              class="px-6 py-4 max-w-lg font-medium text-gray-900 whitespace-nowrap truncate"
            >
              {{ el.id }}
            </th>
            <td class="px-6 py-4"><ul>
              <li v-for="(doc, index) in el.docs" :key="index"> {{ doc }} </li>
            </ul></td>
            <td class="px-6 py-4">{{ el.group }}</td>
            <td class="px-6 py-4">{{ el.name }}</td>
            <td class="px-6 py-4">{{ el.tnved }}</td>
            <td class="px-6 py-4">{{ el.equipment_user_len }}</td>
            <td class="px-6 py-4">{{ el.equipment_find_len }}</td>
            <td class="px-6 py-4">{{ Math.round(el.similarity_score*100) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div>
      <ModalWindow :id="el.id" v-if="isModalOpen" @close="isModalOpen = false" />
    </div>
  </div>
</template>
<script>
import ModalWindow from "@/components/ModalWindow.vue";
export default {
  components: { ModalWindow },
  props: {
    table_data: Array,
  },
  data() {
    return {
      isModalOpen: false,
    };
  },
  emits: ["close"],
  methods: {
    alert_fun(el) {
      alert(el);
    },
  },
};
</script>
