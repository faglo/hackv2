<template>
  <div class="login">
    
    <no-ssr>
      <swipe-modal
        v-model="isModal"
        contents-height="50vh"
        border-top-radius="30px"
        background-color="#28282828"
        contents-width="390px"
      >
        <div class="modal">
            <h2 class="mb-40">Регистрация</h2>
            <div class="modal__inputs">
                <UiInput 
                  class="mb-15" 
                  :placeholder="'Фамилия'"  
                  :value="last_name"
                  @onChange="last_name = $event.target.value"
                />
                <UiInput 
                  class="mb-15" 
                  :placeholder="'Имя'"
                  :value="first_name"
                  @onChange="first_name = $event.target.value"
                />
                <UiInput  
                  class="mb-15" 
                  :placeholder="'Отчество'"  
                  :value="third_name"
                  @onChange="third_name = $event.target.value"
                />
                <UiInput 
                  class="mb-30" 
                  :placeholder="'Пароль'" 
                  ftype="password"
                  :value="password"
                  @onChange="password = $event.target.value" 
                />
                <hr class="mb-20">
            </div>
            <UiButton class="mb-20" :img-width="90" :img-height="16" :img-props="'/imgs/gos.svg'" >Получить через</UiButton>
            <UiButton 
              @click.native="swModalsPTS()" 
              class="mb-20"
            >Ввести данные ПТС вручную</UiButton>
            <UiButton @click.native="swModals()" class="mb-20" :bgColor="'black'">Скнировать ПТС по фото</UiButton>

        </div>
      </swipe-modal>
    </no-ssr>
    <!-- ПТС вручную -->
    <no-ssr>
      <swipe-modal
        v-model="isModal3"
        contents-height="75vh"
        border-top-radius="30px"
        background-color="#28282828"
        contents-width="390px"
      >
      <div class="modal">
        <h2 class="mb-40">Регистрация</h2>
        <UiInput class="mb-15" :placeholder="'Индентификационный номер (VIN)'" />
        <UiInput class="mb-15" :placeholder="'Модель'" />
        <UiInput class="mb-15" :placeholder="'Модель авто'" />
        <UiInput class="mb-15" :placeholder="'Тип двигателя'" />
        <UiInput class="mb-35" :placeholder="'Цвет кузова'" />
        <UiButton  class="mb-20" :bgColor="'black'" >
          <p style="color : #BCED09; font-weight: 600">
            Зарегистрироваться
          </p>
        </UiButton>
      </div>
    </swipe-modal>
    </no-ssr>
    <!-- ПТС вручную -->
    <!-- Вторая модалка -->
    <no-ssr>
      <swipe-modal
        v-model="isModal2"
        contents-height="30vh"
        border-top-radius="30px"
        background-color="#28282828"
        contents-width="390px"
      >
        <div class="modal">
          <div class="mb-50" style="display: flex; align-items: center;">
            <UiButton style="margin-right : 15%" @click.native="isModal2 = false" onlyIcon :imgWidth="11" :img-height="14" :icon-props="'/icons/arrow.svg'" greenSh :bgColor="'black'" />
            <h2>Регистрация</h2>
           
          </div>
            
            <p class="mb-25">Загрузите данные ПТС автоматически:</p>
            <div style="display: flex; flex-direction: column; gap: 35px; padding-bottom: 20px">
              <input id="fileUpload" type="file" hidden/>
              <div style="display: flex; align-items: center; justify-items: center; width: 100%">
                <UiButton dashed :img-width="40" :img-height="40" :img-props="'/icons/docico.svg'" @click.native="chooseFiles()" style="margin-left: auto; margin-right: auto">Загрузите файл</UiButton>
                <!-- <UiButton dashed :img-width="40" :img-height="40" :img-props="'/icons/camera.svg'" >Сделайте снимок</UiButton> -->
              </div>
            </div>
        </div>
      </swipe-modal>
    </no-ssr>
    
    <div class="login__container">
    <h1 class="mb-10 txt-black-bold">Вход</h1>
    <UiInput  class="mb-10" :placeholder="'Логин'" :icon="'/icons/man.svg'" />
    <UiInput class="mb-20" :placeholder="'Пароль'" :icon="'/icons/lock.svg'" />
    <UiButton @click.native="$router.push('/mainPage')" class="mb-20" :bg-color="'green'" >Войти</UiButton>
    <div class="login__quest">
        <p class="mb-25">Забыли пароль?</p>
        <div class="login__hr">
            <hr />
            <p>Или</p>
            <hr />
        </div>
        <p @click="isModal = true" class="mb-20 line curPr">Регистрация</p>
    </div>
    <UiButton :img-width="90" :img-height="16" :img-props="'/imgs/gos.svg'" class="mb-10">Войти с помощью</UiButton>
    <UiButton>Я доверенное лицо</UiButton>
    
</div>
  </div>
</template>

<script>
import UiButton from '../components/ui-kit/UiButton.vue'
import UiInput from '../components/ui-kit/UiInput.vue'
import { ref } from '@nuxtjs/composition-api'

export default {
  components : {UiButton, UiInput},
  data() {
    return {
      first_name: "",
      last_name: "",
      third_name: "",
      password: "",
    }
  },
  setup(props) {
    const isModal = ref(false);
    const isModal2 = ref(false);
    const isModal3 = ref(false);
    function swModals () {
        this.isModal = false
        this.isModal2 = true
    }
    function swModalsPTS () {
        this.isModal = false
        this.isModal3 = true
    }
    return { isModal ,isModal2, isModal3, swModals, swModalsPTS }
  },
  methods: {
    fetchData() {
      this.$axios.$get('https://jsonplaceholder.typicode.com/posts')
        .then((res) => {
          this.posts = res
        })
    },
    chooseFiles: function() {
        document.getElementById("fileUpload").click()
    },
  }
}
</script>

<style lang="scss" scoped>
.login {
    background: $color-dark;
    padding: 0 25px;
    @include fullHeight;
    display: flex;
    align-items: center;
    &__container {
        width: 100%;
        padding: 36px 25px;
        padding-bottom: 22px;
        border-radius: 30px;
        background: $color-white;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        
    }
    &__quest {
        font-size: 13px;
        width: 100%;
    }
    &__hr {
        display: flex;
        margin-bottom: 17px;
        align-items: center;
        gap: 20px;
    }
}
.modal {
    text-align: center;
    padding: 0 32px;
    margin-top: 25px;
}
</style>