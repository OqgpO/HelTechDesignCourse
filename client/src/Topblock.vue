<template>
  <div class="topBlock">
      <menutop></menutop>
      <logo></logo>
      <actionbutton class="link1"></actionbutton><actionbutton class="link2"></actionbutton>
    </div>
</template>

<script>
import Menutop from './Menutop.vue'
import Logo from './Logo.vue'
import Actionbutton from './ActionButton.vue'

export default {
  data () {
    return {
      msg: 'This is top block'
    }
  },
    components: {
        Menutop,
        Logo,
        Actionbutton
    }
}
</script>

<style lang="scss">
@import "style/settings.scss";
.topBlock {
    background-image: repeating-linear-gradient(315deg, $primary-color, $secondary-color);
    position: fixed;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 200px;

    .link1 {
        position: absolute;
        right: 10px;
        bottom: 10px;
    }
    .link2 {
        position: absolute;
        right: 110px;
        bottom: 10px
    }
}
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
