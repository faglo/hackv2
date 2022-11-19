<template>
    <yandex-map
      :coords="coords"
      :controls="[]"
      :zoom="zoom"
      @map-was-initialized="initHandler"
      :options="{ 
        suppressMapOpenBlock: true,
        autoFitToViewport: 'always'
      }"
      :cluster-callbacks="{ '1': { click: getDataPoint }}"
      :cluster-options="{
        1: { 
          clusterDisableClickZoom: false, 
          hasBalloon: false,
          clusterLayout: ['<div class=cluster-icon>{{ properties.geoObjects.length }}</div>'].join('')
      }}"
    >
      <ymap-marker
        v-for="(location, index) in placemarks"
        :key="index"
        :marker-id="index"
        marker-type="placemark"
        :coords="location"
        :callbacks="{ click: getDataPoint }"
        cluster-name="1"
      ></ymap-marker>
    </yandex-map>
  </template>
  
  <script>
  export default {
    components: {},
    props: {
      placemarks: {
        type: Array,
        required: true
      },
      coords: {
        type: Array,
        required: true
      },
      zoom: {
        type: Number,
        default: 12,
        required: true
      }
    },
    data() {
      return {
        map: {}
      };
    },
    methods: {
      getDataCluster(obj) {
        const clust = this.map.geoObjects.get(0);
        this.map.setBounds(clust.getBounds());
        this.$emit("set-coords", obj.get("coords"));
        this.$emit("get-data-point", obj.get("coords").join());
      },
      getDataPoint(obj) {
        const coords = obj.get("coords");
        console.log(coords, "1");
  
        this.$emit("set-coords", coords);
        this.$bus.$emit("get-data-point", coords.join());
      },
      initHandler(obj) {
        this.map = obj;
      }
    }
  };
  </script>
  
  <style scoped>
  .ymap-container {
    height: 100%;
  }
  
  .cluster-icon {
    background: lime;
    color: tomato;
  }
  </style>
  
  