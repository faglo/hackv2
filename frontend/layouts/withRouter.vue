<template>
    <div class="withRouter">
        <main class="main-withRouter">
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