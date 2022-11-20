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
      zoom: 15,
       items: [
        [45.037259, 38.995770],
        [45.020955, 38.964089],
        [45.039708, 38.973505],
        [45.017935, 38.928755],
        ],
      coords: [45.037257, 38.995616],
      
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