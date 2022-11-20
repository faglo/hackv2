<template>
  <div class="detect">
    <no-ssr>
      <swipe-modal
        v-model="modal"
        contents-height="70vh"
        border-top-radius="30px"
        background-color="#28282828"
        contents-width="390px"
      >
    <div class="evo">
        <h1 class="mb-40">Эвакуатор</h1>
        <div style="display: flex; flex-direction:column;align-items:center">
            <img class="mb-50" src="/imgs/mapFull.svg" alt="">
            <img class="mb-30" src="/imgs/route.svg" alt="">
            <UiButton class="mb-20" @click.native="modal = false" :bgColor="'black'" :imgWidth="140" :img-height="10"  :img-props="'/icons/arrowBig.svg'">Заказать</UiButton>

        </div>
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
    <div v-for="(car, id) in carSet" :key="id">
        <div class="detect__main">
            <div class="detect__main__titles">
                <div>
                    <p style="font-size: 28px; font-weight : 400; color : white">{{car.carName}} км</p>
                    <p  style="font-size: 14px; font-weight : 400; color : #BCED09"> {{car.fullCarName}}</p>
                </div>
                <div>
                    <p style="font-size: 28px; font-weight : 400; color : white">{{car.outOfKm}} км</p>
                    <p style="font-size: 14px; font-weight : 400; color : #BCED09">{{car.outOfHrs}}</p>
                </div>
            </div>
            <div class="detect__all">
                <img src="/imgs/carTesla.png" alt="">
            <div style="display: flex; flex-direction : column; gap : 23px">
                <div class="detect__main__delivery">
                    <p style="font-weight: 600">Доставка аккумулятора</p>
                    <div class="detect__main__delivery__card">
                        25 %
                    </div>
                    <div class="detect__main__delivery__card">
                        50 %
                    </div>
                    <div class="detect__main__delivery__card">
                        75 %
                    </div>
                </div>
                <div class="battery">
                    <div class="battery__title">Сухая мойка</div>
                    <div class="battery__fill">60%</div>
                </div>
            </div>
        </div>
        <div class="helpers">
            <img class="helpers__card"   src="/icons/carLook.svg" alt="">
            <img class="helpers__card" src="/icons/monitor.svg" alt="">
            <img class="helpers__card--red"   src="/icons/tools.svg" alt="">
            
            </div>
        
        </div>
    </div>
  </div>
</template>

<script>
import { ref } from '@nuxtjs/composition-api'
export default {
    layout : 'withRouter',
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
        ],
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
}
.detect {
    &__all {
        display: flex;
        align-items: flex-start;
        gap: 22px;
    }
    &__main {
        position: relative;
        &__titles {
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: absolute;
            padding: 22px;
            gap: 78px;
        }
        &__delivery{
            max-width: 145px;
            display: flex;
            gap: 15px;
            align-items: center;
            text-align: center;
            padding-top: 10px;
            padding-bottom: 30px;
            box-shadow: -4px 4px 13px 5px #BCED094D;
            border-radius: 30px;
            margin-top: 90px;
            flex-direction: column;
            background: white;
            &__card {
                padding: 7px 33px;
                background: #BCED09;
                border-radius: 20px;
                color: white;
            }
        }
    }
}
.battery {
        @include card;
        padding: 18px 6px 6px 6px;
        height: 218px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        text-align: center;
        background: #EDFABC;

        &__fill {
            background: #BCED09;
            color: $color-def;
            border-radius: 25px;
            padding: 50px 30px;
        }
    }
    .helpers {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin: 30px 0;
        &__card {
            padding: 12px;
            box-shadow: -10px 8px 10px 2px #FFFFFF26;
            background: white;
            border-radius: 20px;
            &--red{ 
                padding: 12px;
                box-shadow: -10px 8px 10px 2px #FFFFFF26;
                background: #EE2F53;
                border-radius: 20px;
                
            }
        }
    }
</style>