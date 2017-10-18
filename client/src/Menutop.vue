<template>
  <div class="menu">{{ msg }}</div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Menu top component'
    }
  }
}
</script>

<style lang="scss">
    @import "style/settings.scss";
    .menu {
        color: $tertiary-color;
        text-align: right;
    }
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
