<template>
  <button 
  :class="[
   bgColor && `uiButton--${bgColor}`,
   imgProps &&  'uiButton--withImg' ,
   onlyIcon && 'uiButton--onlyIcon' ,
   dashed && 'uiButton--dashed'
   ]"
   class="uiButton">
    <template v-if="!onlyIcon">
        <slot />
    </template>  
    <img :class="greenSh && 'green-shadow' " v-if="iconProps && onlyIcon" :src="iconProps" 
    :width="imgWidth"
    :height="imgHeight"
    />
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
        },
        iconProps : {
            type : Number,
            default : 0,
        },
        onlyIcon : { 
            type : Boolean,
            default: false
        },
        dashed : {
            type : Boolean,
            default : false
        },
        greenSh : {
            type : Boolean,
            default: false
        }
    }
}
</script>

<style lang="scss" scoped>
.uiButton {
    width: 100%;
    border-radius: 62px;
    cursor: pointer;
    background: $color-def;
    padding: 16px 0;
    color : $color-btnText;
    border: none;
    box-shadow: 0px 1.4379562139511108px 4.313868522644043px 0px #13124212;
    &--green {
        color: $color-def;
        background: $color-green;
        box-shadow: 0px 5.751824855804443px 15.81751823425293px 0px #20202033;
    }
    &--greenBorder { 
font-size: 16px;
font-weight: 500;
color : black;
border: 2px solid #BCED09;

line-height: 14px;
letter-spacing: 0em;
text-align: center;
        background: white;

    }
    &--fullgreen {
        color : #BCED09;
        background: none;
        border: 2px solid #BCED09;
    }
    &--fullWhite {
        color : white;
        border: 1px solid white;
        background: none;
    }
    &--black {
        background: $color-dark;
        color: $color-def;
        font-weight: 700;
        font-size: 16px;
        box-shadow: 0px 1.4379562139511108px 4.313868522644043px 0px #13124212;
        border: 0.72px solid #EFF0F6;
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
    &--onlyIcon {
        border-radius: 19px;
        padding: 20px;
        width: unset;
    }
    &--dashed { 
        border: 3px dashed #000000;
        max-width: 155px;
        flex-direction: column;
        padding: 30px;
        font-weight: 700;
        border-radius: 30px;
        color: $txt-dark;
    }
}
.green-shadow{
    filter : drop-shadow(3px 3px 2px #BCED09);
}
</style>