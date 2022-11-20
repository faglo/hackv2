<template>
    <div class="uiInput__container">
        <input :placeholder="placeholder" class="uiInput" :type="ftype" :value="value" v-on:change="onChange">
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
        },
        ftype: {
            type: String,
            default: 'text'
        },
        value: {
            type: String,
            default: ''
        },
        onChange: {
            type: Function,
            default: () => {}
        }
    }
}

</script>
<style lang="scss" scoped>
.uiInput {
    border: none;
    color: $color-btnText;
    font-weight: 400;
    font-size: 15px;
    width: 100%;
    &::placeholder {
        color: $color-btnText;
        font-weight: 400;
        font-size: 15px;
    }
    &:focus {
        outline: none;
    }
    &__container {
        width: 100%;
        justify-content: space-between;
        border-radius: 33px;
        background: $color-def;
        padding: 18px 29px;
        color: white;
        box-shadow: 0px 1.4379562139511108px 4.313868522644043px 0px #13124212;
        border: 0.72px solid #EFF0F6;
        display: flex;
        max-width: --webkit-fill-available;
    }
    &__img {
        max-width: 20px;
    }
}

</style>