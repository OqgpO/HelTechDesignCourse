<template>
  <div class="eventsapp">{{ msg }}</div>
</template>

<script>
import Currentevent from './Currentevent.vue'
import Smallevent from './SmallEvent.vue'

export default {
  data () {
    return {
      msg: 'Events block'
    }
  }
}
</script>

<style lang="scss">
    @import "../style/settings.scss";
    .eventsapp {
        font: 100% $font-stack;
        height: 200px;
        color: $tertiary-color;
        text-align: left;
        margin-top: 0px;

    }
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
