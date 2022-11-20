<template>
  <div class="account">
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
    <div class="account__header">
        <div style="display: flex; align-items: center; gap : 5px">
            <UiButton @click.native="$router.back()" onlyIcon :imgWidth="11" :img-height="14" :icon-props="'/icons/arrowWhite.svg'" greenSh  />
            <div style="color : white; font-size: 20px;" >Привет, <span>{{shortName}}</span></div>
        </div>
        <div style="display : flex; position: relative; align-items: center">
          <UiButton @click.native="modal = true" style="position : absolute; right: 80%;" onlyIcon :imgWidth="30" :img-height="30" :icon-props="'/icons/warn.svg'" />
          <img style="z-index: 1" height="66" width="66"  src="/imgs/dude.png" alt="">
        </div>
    </div>
    <div class="account__ava">
        <img class="bordered-dude" src="/imgs/dude.png" alt="">
    </div>
    <h1 class="mb-15" style="font-size: 24px; color : white ;text-align : center">{{name}}</h1>
    <div  style=" margin : 0 auto; max-width: 142px;" >
        <ui-button  style="padding: 8px 0" class="mb-25" bgColor="fullWhite" >Ваши данные</ui-button>
    </div>
    <ui-button class="mb-20" bgColor="greenBorder" >Добавить доверенное лицо</ui-button>
    <div class="mb-25">

    
    <div class="account__docs">
        <div class="mb-20" style="display: flex; justify-content: space-between; align-items: center;">
            <h2>Документы</h2>
            <UiButton style="
            max-width: 85px; padding: 5px 0; border: 1px solid black; color:  black"
            >Все</UiButton>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
            <div v-for="(doc, id) in docsSet" :key="id" class="account__docs__loop">
                <div class="doc">
                    <img width="30" height="30" :src="doc.icon" alt="">
                    <p>{{doc.name}}</p>
                </div>
            </div>
        </div>
        <UiButton :bgColor="'black'" :imgWidth="140" :img-height="10"  :img-props="'/icons/arrowBig.svg'">Добавить</UiButton>
    </div>
</div>
    <div class="account__cars">
        <div class="account__cars__title">Ваши машины:</div>
        <div class="scroll">   
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
</div>
    </div>
    <div style="margin : 0 auto; max-width: 144px " @click="$router.push('/')">
        <UiButton :bgColor="'fullgreen'"   style="border-radius: 20px;" :imgWidth="20" :img-height="20" :img-props="'/icons/out.svg'">Выйти</UiButton>
    </div>
  </div>
</template>

<script>
import { ref } from '@nuxtjs/composition-api'
import UiButton from '../components/ui-kit/UiButton.vue'
export default {
    layout : 'withRouter',
  components: { UiButton },
  setup(){
    const modal = ref(false);
    return { modal }
  },
    data () {
        return {
            name : 'Марк Иванов',
            shortName : 'Марк',
            yourCars : {
                
            },
            carSet : [
            {
                carName : 'Model 3',
                fullCarName : 'Tesla, 2018',
                outOfKm : '68',
                outOfHrs : '1 ч 36 мин',
                carImg : '/imgs/tesla.png',
                battery : '40%'
             },
            {
                carName : 'Model 3',
                fullCarName : 'Tesla, 2018',
                outOfKm : '68',
                outOfHrs : '1 ч 36 мин',
                carImg : '/imgs/tesla.png',
                battery : '40%'
             },
            {
                carName : 'Model 3',
                fullCarName : 'Tesla, 2018',
                outOfKm : '68',
                outOfHrs : '1 ч 36 мин',
                carImg : '/imgs/tesla.png',
                battery : '40%'
             },
            ],
            docsSet : [
                {
                    name : 'Паспорт РФ',
                    icon : '/icons/accPass.svg',
                },
                {
                    name : 'Снилс',
                    icon : '/icons/accMe.svg',
                },
                {
                    name : 'Мед. полис',
                    icon : '/icons/accPolis.svg',
                },
            ]
        }
    }
}
</script>

<style lang="scss" scoped>
.mainPage {
&__car {
        @include card;
        width: 308px;
        &__title{ 
            display: flex;
            color: black;
            align-items: center;
            justify-content: space-between;
        }
    }
}
.account {
    // padding: 30px 20px;
    padding-bottom: 20px;
    &__header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    &__ava {
        max-width: fit-content;
        margin: 0 auto;
    }
    &__docs {
        border-radius: 30px;
        max-width: 348px;
        margin: 0 auto;
        padding: 15px 20px;
        background: #F8F8F8;
    }
    &__cars {
        &__title {
            font-size: 24px;
            color: #BCED09;
            font-weight: 900;
            margin-bottom: 20px;
        }
    }
}
.bordered-dude {
    border-radius: 50%;
    width: 140px;
    height: 140px;
    border: 1px dashed #BCED09;
        border-radius: 50%;
        padding: 10px;
}
.doc {
    display: flex;
    flex-direction: column;
    gap: 22px;
    padding: 40px 10px;
    padding-bottom: 15px;
    box-shadow: 1px 4px 9px 0px #BCED0940;
    border-radius: 10px;
    // width: 100px;
    align-items: center;
    text-align: center;
}
</style>