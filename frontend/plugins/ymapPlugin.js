import Vue from "vue";
import YmapPlugin from "vue-yandex-maps";

const settings = {
  apiKey: "8204acea-1467-4fff-8a46-548a6f8758a6",
  lang: "ru_RU",
  coordorder: "latlong",
  enterprise: false,
  version: "2.1",
}; // настройки плагина

Vue.use(YmapPlugin, settings);