<template>
  <div class="router">
    <div class="router__row" >
        <div class="router__route" @click="$router.push('/mainPage')">
            <img  src="/icons/carico.svg" alt="">
        </div>
        <div class="router__route" @click="$router.push('/mainPage')">
            <img  src="/icons/carico.svg" alt="">
        </div>
        <div class="router__route" @click="$router.push('/mainPage')">
            <img  src="/icons/carico.svg" alt="">
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.router {
    @include card;
    box-shadow: 6px 6px 43px 0px #BCED094D;
    &__row {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

}
</style>