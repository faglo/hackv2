<template>
  <div class="account">
    <div class="account__header">
        <div>Привет, <span>Марк</span></div>
        <div style="display : flex; position: relative; align-items: center">
          <UiButton style="position : absolute; right: 80%;" onlyIcon :imgWidth="22" :img-height="22" :icon-props="'/icons/lupa.svg'" />
          <img style="z-index: 1" height="66" width="66"  src="/imgs/dude.png" alt="">
        </div>
    </div>
    <div class="account__ava">
        <img class="bordered-dude" src="/imgs/dude.png" alt="">
    </div>
    <div  style=" margin : 0 auto; max-width: 142px;" >
        <ui-button  style="padding: 8px 0" class="mb-25" bgColor="fullWhite" >Ваши данные</ui-button>
    </div>
    <ui-button class="mb-20" bgColor="greenBorder" >Добавить доверенное лицо</ui-button>
    <div class="account__docs ">
        <div class="mb-20" style="display: flex; justify-content: space-between; align-items: center;">
            <h2>Документы</h2>
            <UiButton style="max-width: 85px; padding: 5px 0;">Все</UiButton>
        </div>
        <div style="display: flex; gap: 13px">
            <div v-for="(doc, id) in docsSet" :key="id" class="account__docs__loop">
                <div class="doc">
                    <img width="30" height="30" :src="doc.icon" alt="">
                    <p>{{doc.name}}</p>
                </div>
            </div>
        </div>
        <UiButton :bgColor="'black'" :imgWidth="140" :img-height="10"  :img-props="'/icons/arrowBig.svg'">Добавить</UiButton>
    </div>
    <div class="account__cars">
        <div class="account__cars__title">Ваши машины:</div>
        <div></div>
    </div>
    <div style="margin : 0 auto; max-width: 144px ">
        <UiButton :bgColor="'fullgreen'"  style="border-radius: 20px;" :imgWidth="20" :img-height="20" :img-props="'/icons/out.svg'">Выйти</UiButton>
    </div>
  </div>
</template>

<script>
import UiButton from '../components/ui-kit/UiButton.vue'
export default {
    // layout : 'withRouter',
  components: { UiButton },
    data () {
        return {
            name : 'Марк Иванов',
            shortName : 'Марк',
            yourCars : {
                
            },
            docsSet : [
                {
                    name : 'Паспорт РФ',
                    icon : '/icons/accMe.svg',
                },
                {
                    name : 'Снилс',
                    icon : '/icons/accMe.svg',
                },
                {
                    name : 'Мед. полис',
                    icon : '/icons/accMe.svg',
                },
            ]
        }
    }
}
</script>

<style lang="scss" scoped>
.account {
    padding: 30px 20px;
    &__header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    &__ava {
        border: 1px dashed #BCED09;
        max-width: fit-content;
        border-radius: 50%;
        padding: 10px;
        margin: 0 auto;
    }
    &__docs {
        border-radius: 30px;
        max-width: 348px;
        margin: 0 auto;
        padding: 15px 20px;
        background: #F8F8F8;
    }
}
.bordered-dude {
    border-radius: 50%;
    width: 140px;
    height: 140px;
}
.doc {
    display: flex;
    flex-direction: column;
    gap: 22px;
    padding: 40px 10px;
    padding-bottom: 15px;
    box-shadow: 1px 4px 9px 0px #BCED0940;
    border-radius: 10px;
    width: 100px;
    align-items: center;
    text-align: center;
}
</style>