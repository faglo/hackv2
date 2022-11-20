<template>
    <div class="withRouter">
        <main 
        :class="$route.path != '/map' ? 'main-withRouter' : 'main-map' " 
        >
            <Nuxt />
            <BottomRouter />
        </main>
    </div>
</template>

<script>
import BottomRouter from '../components/BottomRouter.vue'
export default {
  components: { BottomRouter },

}
</script>

<style lang="scss" scoped >
.withRouter {
    display: flex;
    flex-direction: column;
}
</style>