<template>
  <div class="mainPage">
    <no-ssr>
      <swipe-modal
        v-model="modal"
        contents-height="35vh"
        border-top-radius="30px"
        background-color="#28282828"
        contents-width="390px"
      >
      <div class="warn">
        <div class="warn__title">Внимание!</div>
        <div class="warn__main">
          <p>В вашем автомобиле прозошла поломка. </p>
          <hr>
          <div style="display: flex; gap: 10px; aling-items:center">
            <img src="/icons/maps.svg" alt="">
            <span>Ближайший сервис в  300м от вас</span>
          </div>
        </div>
        <UiButton @click.native="$router.push('/detect')" :bgColor="'black'" :imgWidth="140" :img-height="10"  :img-props="'/icons/arrowBig.svg'">Посмотреть</UiButton>

      </div>
      </swipe-modal>
 </no-ssr> 

    <div class="mainPage__title mb-20">
        <UiSelect :options-set="options" />    
        <div style="display : flex; position: relative; align-items: center">
          <UiButton @click.native="modal = true" style="position : absolute; right: 80%;" onlyIcon :imgWidth="30" :img-height="30" :icon-props="'/icons/warn.svg'" />
          <img @click="$router.push('/account')" class="dude"  src="/imgs/dude.png" alt="">
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
            <img style="border-radius : 30px" width="100%" :src="car.carImg" alt="">
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
import { ref } from '@nuxtjs/composition-api'
import UiButton from '../components/ui-kit/UiButton.vue';
import UiSelect from '../components/ui-kit/UiSelect.vue'
export default {
    layout : 'withRouter',
  components: { UiSelect, UiButton },
  setup(){
    const modal = ref(false);
    return { modal }
  },
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
          z-index: 1;
            width: 65.76px;
            height: 65.76px;
        }
    }
    &__car {
        @include card;
        &__title{ 
            display: flex;
            color: black;
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