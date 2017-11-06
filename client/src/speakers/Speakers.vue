<template>
  <h1 class="speakersapp">{{ msg }}</h1>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Speakers block'
    }
  }
}
</script>

<style lang="scss">
    @import "../style/settings.scss";
    .speakersapp {
        font: 100% $font-stack;
        height: 200px;
        margin-top: 0px;
        margin-bottom: 0px;
        color: $tertiary-color;
        text-align: left;
    }
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
