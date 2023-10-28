<template>
  <body class="bg-whitesmoke font-rale">
    <Header></Header>
    <div class="">
      <div class="xl:px-28 pt-4 shadow-lg">
        <div>
          <LogoTurik />
        </div>
        <div class="pt-5">
          <FormsFile />
        </div>
        <div class="pt-10 border-t-2 border-[#e40046]">
          <Form />
        </div>
        <div class="flex flex-col border-t-2 border-[#e40046] pt-4">
          <RightAside />
        </div>
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
import LogoTurik from "@/components/LogoTurik.vue";
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
    LogoTurik,
  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>
