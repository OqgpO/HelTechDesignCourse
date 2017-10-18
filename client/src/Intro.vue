<template>
  <div class="intro">{{ msg }}</div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Intro'
    }
  }
}
</script>

<style lang="scss">
  @import "style/settings.scss";
  .intro {
    font: 200% $font-stack;
    color: primary-color;
    margin-top: 200px;
    height: 200px;
}
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
