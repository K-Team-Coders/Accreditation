<template>
  <body class="bg-whitesmoke">
    <Header></Header>
    <div class="flex">
      <div class="px-36 pt-10 shadow-lg w-9/12">
        <div class="flex justify-center">
          <FormsFile />
        </div>
        <div class="mt-4">
          <TableSite />
        </div>
        <div class="mt-16 flex justify-center">
          <Form />
        </div>
        <div class="grid grid-cols-2 gap-2 mt-10 mb-4">
          <Cards name="book" text="12367-123" title="ГОСТ: " />
          <Cards name="code" text="1746293568487" title="ТН ВЕД: " />
          <Cards
            name="tech"
            text="станок некачественный"
            title="Оборудование: "
          />
          <Cards
            name="list"
            text="набитый мясом холодильник"
            title="Группа продукции: "
          />
        </div>
        <div class="flex justify-center mb-6">
          <DownloadButtonGost />
        </div>
      </div>
      <div class="w-3/12 flex">
        <RightAside />
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Form from "@/components/Form.vue";
import FormsFile from "@/components/FormsFile.vue";
import Cards from "@/components/Cards.vue";
import DownloadButtonGost from "@/components/DownloadButtonGost.vue";
import TableSite from "@/components/TableSite.vue";
import { mapActions, mapGetters } from "vuex";
import RightAside from "@/components/RightAside.vue";
export default {
  components: {
    Header,
    Footer,
    Form,
    FormsFile,
    Cards,
    DownloadButtonGost,
    TableSite,
    RightAside,
  },
  data() {
    return {
      choosed_uav: "",
      choosed_range: 0,
      current_icon: "",
      selected: "Все страны",
    };
  },
  computed: {
    ...mapGetters(["allCountries", "allUAVS"]),
    filteredList() {
      let count = this.selected;
      return this.allUAVS.filter(function (elem) {
        if (count === "Все страны") return true;
        else return elem.country.indexOf(count) > -1;
      });
    },
  },
  methods: {
    ...mapActions([
      "GET_ALLCOUNTRIES",
      "CHANGE_UAV",
      "CHANGE_RANGE",
      "CHANGE_ICON",
      "GET_ALLUAVS",
    ]),
    click_drone(uav, range, max_speed) {
      this.choosed_uav = uav;
      this.choosed_range = range;
      this.CHANGE_UAV(uav);
      this.CHANGE_RANGE(range);
      if (0 <= max_speed && max_speed < 92.6) {
        this.current_icon =
          "https://cdn-icons-png.flaticon.com/512/974/974510.png";
      } else if (92.6 <= max_speed && max_speed < 463) {
        this.current_icon =
          "https://cdn-icons-png.flaticon.com/512/2792/2792018.png";
      } else {
        this.current_icon =
          "https://cdn-icons-png.flaticon.com/512/2223/2223188.png";
      }
      this.CHANGE_ICON(this.current_icon);
    },
  },
  async created() {
    this.GET_ALLUAVS();
  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>
