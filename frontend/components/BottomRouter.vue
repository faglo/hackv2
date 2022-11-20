<template>
  <div :class="$route.path === '/map' && 'router--absolute'" class="router">
    <div v-if="$route.path != '/map'" class="router__row" >
        <div class="router__route" @click="$router.push('/detect')">
            <img 
            :src=" $route.path === '/detect' 
                ? '/icons/routs/unnoir/about.svg'
                : '/icons/routs/noir/about.svg' 
            " 
            />
        </div>
        <div class="router__route" @click="$router.push('/mainPage')">
            <img  
            :src=" $route.path === '/mainPage' 
                ? '/icons/routs/unnoir/car.svg'
                : '/icons/routs/noir/car.svg' 
            "
            />
        </div>
        <div class="router__route" @click="$router.push('/map')">
            <img 
            :src=" $route.path === '/map' 
                ? '/icons/routs/unnoir/map.svg'
                : '/icons/routs/noir/map.svg' 
            "
            />
        </div>
    </div>
    <div class="router__map" v-else>
        <img src="/icons/mapGroup.svg" alt="">
        <div class="router__map__txt">
            <p>Ваше местоположение</p>
            <div>
                <p>Введите адрес</p>
                <p>70% энергии осталось</p>
            </div>
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
    &--absolute {
        position: absolute;
        bottom: 27px;
        max-width: 300px;
        width: 100%;
        margin:  0 auto;
    }
    &__row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 50px;
    }
    &__route {
        cursor: pointer;
    }
    &__map {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        &__txt {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
    }
}
.recolor-icon {
    color: black;

}
</style>