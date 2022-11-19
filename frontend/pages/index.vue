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
                <UiInput  class="mb-15" :placeholder="'Фамилия'"  />
                <UiInput class="mb-15" :placeholder="'Имя'"  />
                <UiInput  class="mb-15" :placeholder="'Отчество'"  />
                <UiInput class="mb-30" :placeholder="'Пароль'" />
                <hr class="mb-20">
            </div>
            <UiButton class="mb-20" :img-width="90" :img-height="16" :img-props="'/imgs/gos.svg'" >Получить через</UiButton>
            <UiButton @click.native="swModals()" class="mb-20">Ввести данные ПТС вручную</UiButton>
            <UiButton class="mb-20" :bgColor="'black'">Скнировать ПТС по фото</UiButton>

        </div>
      </swipe-modal>
    </no-ssr>
    <!-- Вторая модалка -->
    <no-ssr>
      <swipe-modal
        v-model="isModal2"
        contents-height="90vh"
        border-top-radius="30px"
        background-color="#28282828"
        contents-width="390px"
      >
        <div class="modal">
            <h2 class="mb-50">Регистрация</h2>
            
            <div style="display: flex; gap: 35px">
                <UiButton dashed class="mb-20">Загрузите файл</UiButton>
                <UiButton dashed class="mb-20" :img-width="40" :img-height="40" :img-props="'/icons/camera.svg'" >Сделайте снимок</UiButton>
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
  setup(props) {
    const isModal = ref(true);
    const isModal2 = ref(true);
    function swModals () {
        this.isModal = false
        this.isModal2 = true
    }
    return { isModal ,isModal2, swModals }
  },
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