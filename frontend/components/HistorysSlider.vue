<template>
  <div class="slider">
    <UiButton @click.native="$router.back()" onlyIcon :imgWidth="11" :img-height="14" :icon-props="'/icons/arrowWhite.svg'" greenSh  />
    <UiSelect :options-set="options" />
    <img width="66" height="66" src="/imgs/dude.png" />
  </div>
</template>

<script>
import UiButton from './ui-kit/UiButton.vue'
import UiSelect from './ui-kit/UiSelect.vue'
export default {
  components: { UiButton, UiSelect },
    data() {
        return {
            options : ['Зарядки', 'Парковки', 'Сервисные центры', ]
        };
    }
}
</script>

<style lang="scss" scoped>
.slider {
    position: absolute;
    padding: 0 9%;
    padding-top: 33px;
    z-index: 999;
    display: flex;
    gap: 21px;
    align-items: center;
    justify-content: space-between;
}
</style>