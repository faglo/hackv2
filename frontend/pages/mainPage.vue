<template>
  <div class="mainPage">
    <div class="mainPage__title mb-20">
        <UiSelect :options-set="options" />    
        <div>
            <img class="dude"  src="/imgs/dude.svg" alt="">
            <UiButton onlyIcon :imgWidth="22" :img-height="22" :icon-props="'/icons/lupa.svg'" />
        </div>
    </div>
    <div v-for="(car,id) in carSet" :key="id">
        <div class="mainPage__car mb-20">
            <div class="mainPage__car__title mb-10">
                <div>
                    <h1>{{ car.carName }}</h1>
                    <h5>{{ car.fullCarName}}</h5>
                </div>
                <div>
                    <h2>{{ car.outOfKm }} Км</h2>
                    <h5>{{ car.outOfHrs}}</h5>
                </div>
            </div>
            <img width="100%" :src="car.carImg" alt="">
        </div>
        <div class="mainPage__car__img"></div>
    </div>
    <div class="mainPage__info">
        <img src="/imgs/map.svg" alt="">
        <div class="battery">
            <div class="battery__title">Батарея</div>
            <div class="battery__fill">40%</div>
        </div>
    </div>
  </div>
</template>

<script>
import UiButton from '../components/ui-kit/UiButton.vue';
import UiSelect from '../components/ui-kit/UiSelect.vue'
export default {
    layout : 'withRouter',
  components: { UiSelect, UiButton },
  data() {
    return {
        options : ['Tesla', 'Nisan'],
        carSet : [
            {
                carName : 'Model 3',
                fullCarName : 'Tesla, 2018',
                outOfKm : '68',
                outOfHrs : '1 ч 36 мин',
                carImg : '/imgs/tesla.png',
                battery : '40%'
             }
        ]
    };
  }
}
</script>

<style lang="scss" scoped>
.mainPage {
    &__title {
        display: flex;
        justify-content: space-between;
        align-items: center;
        .dude {
            width: 65.76px;
            height: 65.76px;
        }
    }
    &__car {
        @include card;
        &__title{ 
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
    }
    &__info {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .battery {
        @include card;
        padding: 18px 6px 6px 6px;
        height: 218px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        text-align: center;
        &__fill {
            background: #BCED09;
            color: $color-def;
            border-radius: 25px;
            padding: 30px;
        }
    }
}
</style>