<template>
  <div class="currentevent">{{ msg }}</div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Current event'
    }
  }
}
</script>

<style lang="scss">
    @import "../style/settings.scss";
    .currentevent {
        font: 100% $font-stack;
        color: $tertiary-color;
        text-align: left;
    }
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
