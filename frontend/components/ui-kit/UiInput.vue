<template>
    <div class="uiInput__container">
        <input :placeholder="placeholder" class="uiInput" type="text">
        <img :src="icon" class="uiInput__img" />
    </div>
</template>

<script>
export default {
    props : {
        icon : {
            type : String,
            default : ''
        },
        placeholder : {
            type: String,
            default : ''
        }
    }
}

</script>
<style lang="scss" scoped>
.uiInput {
    border: none;
    font-size: 12.94px;
    &:focus {
        outline: none;
    }
    &__container {
        width: 100%;
        justify-content: space-between;
        border-radius: 33px;
        background: $color-def;
        padding: 18px 15px;
        display: flex;
        max-width: --webkit-fill-available;
    }
    &__img {
        max-width: 20px;
    }
}

</style>