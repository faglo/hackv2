<template>
  <select :class="$route.path === '/map' && 'uiSelect--map'" style="
    background-color: white" class="uiSelect">  
    <option
        v-for="option in optionsSet" 
        :key="option.id"
        :value="option"
        >{{option}}
    </option>
  </select>
</template>

<script>
export default {
    props : {
        optionsSet : {
            type : Array,
            default : () => []
        }
    },
    data() {
        return {
            // selected : props.optionsSet
        }
    },  
    created: function() {
        // this.selected = optionsSet.find(i => i.id === this.selected);
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
    &--map {
        width: unset;
    }
}
</style>