<template>
  <button :class="[bgColor && `uiButton--${bgColor}`, imgProps && 'uiButton--withImg']" class="uiButton">

        <slot />

    <img v-if="imgProps"
        :src="imgProps"
        :width="imgWidth"
        :height="imgHeight"
        />
  </button>
</template>

<script>
export default {
    props : {
        bgColor : {
            type : String,
            default : ""
        },
        imgProps : {
            type : String,
            default : ''
        },
        imgWidth : {
            type : Number,
            default : 0,
        },
        imgHeight : {
            type : Number,
            default : 0,
        }
    }
}
</script>

<style lang="scss" scoped>
.uiButton {
    border-radius: 62px;
    cursor: pointer;
    background: $color-def;
    padding: 16px 0;
    color : $color-defText;
    border: none;
    box-shadow: 0px 1.4379562139511108px 4.313868522644043px 0px #13124212;
    &--green {
        color: $color-def;
        background: $color-green;
        box-shadow: 0px 5.751824855804443px 15.81751823425293px 0px #20202033;
    }
    &--withImg {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 11px;
        img {
            max-width: fit-content;
        }
    }
}
</style>