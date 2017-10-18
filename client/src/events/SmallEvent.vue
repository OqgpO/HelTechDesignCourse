<template>
  <div class="smallevent">{{ msg }}</div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Small event for listing'
    }
  }
}
</script>

<style lang="scss">
    @import "../style/settings.scss";
    .smallevent {
        font: 100% $font-stack;
        color: $tertiary-color;
        text-align: left;
    }
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
