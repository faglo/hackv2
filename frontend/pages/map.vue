<template>
  <div style="position : relative">
    <HistorysSlider />
    <section style="height: 100vh">
      <yandex-maps :coords="coords" :placemarks="items" :zoom="zoom" @set-coords="coords = $event"></yandex-maps>
    </section>
  </div>
</template>

<script>
  import YandexMaps from "@/components/YandexMaps";
import HistorysSlider from "../components/HistorysSlider.vue";
  export default {
  components : { YandexMaps, HistorysSlider },
  layout : 'withRouter',
  data () {
    return { 
      zoom: 9,
       items: [
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262],
        [55.771996, 37.622262]
        ],
      coords: [55.636448, 37.675648],
    };
  },
  created() {
    this.$bus.$on("get-data-point", (coords) => {
      console.log(coords);
      // this.queryToGetData(
      //   this.loadMore,
      //   this.currentTab,
      //   START_PAGE,
      //   this.specField.id,
      //   this.searchField,
      //   coords)
    });
  },
  beforeDestroy() {
    this.$bus.$off("get-data-point");
  },
}

</script>

<style>

</style>