<template>
  <h1 class="partnersapp">{{ msg }}</h1>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Partners block'
    }
  }
}
</script>

<style lang="scss">
    @import "../style/settings.scss";
    .partnersapp {
        font: 100% $font-stack;
        color: $tertiary-color;
        text-align: center;
        vertical-align: bottom;
        height: 100px;
        margin-top: 0px;
        margin-bottom: 0px;
    }
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
