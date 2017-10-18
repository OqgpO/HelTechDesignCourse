<template>
<div class="actionbutton"><b>{{ msg }}</b></div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'BUTTON'
    }
  }
}
</script>

<style lang="scss">
  @import "style/settings.scss";

  .actionbutton {
      font: 100% $font-stack;
      color: floralwhite;
      border-color: floralwhite;
      width: 80px;
      height: 30px;
      border-width: 1px;
      border-style: groove;
      border-radius: 4px;

        b {
          position: relative;
          top: 7px;
      }
    }
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
