<template>
  <div class="login">
    <div class="login__container">
    <h1 class="mb-10 txt-black-bold">Вход</h1>
    <UiInput class="mb-10" :placeholder="'Логин'" :icon="'/icons/man.svg'" />
    <UiInput class="mb-20" :placeholder="'Пароль'" :icon="'/icons/lock.svg'" />
    <UiButton class="mb-20" :bg-color="'green'" >Войти</UiButton>
    <div class="login__quest">
        <p class="mb-25">Забыли пароль?</p>
        <div class="login__hr">
            <hr />
            <p>Или</p>
            <hr />
        </div>
        <p class="mb-20 line">Регистрация</p>
    </div>
    <UiButton :img-width="16" :img-height="16" :img-props="'/imgs/gos.svg'" class="mb-10">Войти с помощью</UiButton>
    <UiButton>Я доверенное лицо</UiButton>
    
</div>
  </div>
</template>

<script>
import UiButton from '../components/ui-kit/UiButton.vue'
import UiInput from '../components/ui-kit/UiInput.vue'
export default {
  components: { UiButton, UiInput },

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
    }
    &__hr {
        display: flex;
        margin-bottom: 17px;
        align-items: center;
    }
}

</style>