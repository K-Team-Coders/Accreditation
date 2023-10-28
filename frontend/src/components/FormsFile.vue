<template>
  <div>
  <div class="flex flex-col justify-center items-center px-4 xl:px-0">
    <div
      class="bg-gray-50 2xl:max-w-4xl xl:max-w-3xl lg:max-w-2xl md:max-w-2xl sm:max-w-xl p-4 w-full px-4 py-3 rounded-lg shadow-md"
    >
      <form>
        <div class="flex items-center py-2">
          <input
            v-on:change="handleFilesUpload()"
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
            @click="submitFiles()"
            type="submit"
            class="text-whitesmoke bg-[#e40046] hover:bg-[#ce134b] focus:ring-4 focus:outline-none focus:ring-[#ce134b] font-semibold rounded-lg text-sm w-full sm:w-auto px-4 py-2.5 text-center mt-2"
          >
            Проверить файл
          </button>
        </div>
      </form>
    </div>
  </div>
  <div class="pt-5 pb-16 overflow-x-auto">
    <TableSite />
  </div>
  </div>
</template>

<script>
import TableSite from "./TableSite.vue";
import axios from "axios";
export default {
  components: {
    TableSite,
  },
  data() {
    return {
      is_Error: false,
      files: "",
      text: "",
      isTyping: false,
      is_Loading: false,
      colors: ["#4487BE", "#FF7E00", "#222"],
    };
  },
  methods: {
    submitFiles() {
      console.log(this.files);
      this.is_Loading = true;
      let formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        formData.append("file", file);
      }
      console.log(this.IP);
      axios
        .post(
          `http://${process.env.VUE_APP_USER_IP_WITH_PORT}/check_dataset/`,
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then(function () {
          console.log("SUCCESS!!");
        })
        .catch(function (response) {
          console.log("FAILURE!!");
          if (response.statusCode == 400) {
            alert("Такой файл уже был загружен! Загрузите другой.");
          }
        })
        .finally(function () {
          is_Loading = false;
        });
    },
    handleFilesUpload() {
      this.files = this.$refs.files.files;
    },
  },
};
</script>
