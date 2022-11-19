<template>
  <select class="uiSelect" style="
    background-color: white;">
    <template v-for="option in optionsSet">
        <option>{{option}}</option>
    </template>
  </select>
</template>

<script>
export default {
    props : {
        optionsSet : {
            type : Array,
            default : () => []
        }
    }
}
</script>

<style lang="scss" scoped>
.uiSelect {
    max-width: 160px;
    width: 100%;
    padding: 12px 28px;
    border-radius: 20px; 
    appearance: none; 
    box-shadow: 0px 4px 11px 0px #FFFFFF26;
    overflow: hidden;
    background: url('/icons/selectArrow.svg' ) no-repeat right;

}
</style>