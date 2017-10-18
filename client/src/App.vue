<template>
  <div id="app">
  <topblock></topblock>
  <intro></intro>
  <events></events>
  <speakers></speakers>
  <partners></partners>
  <div class="newsletter">Subscribe</div>
  </div>
</template>

<script>
import Topblock from './Topblock.vue'
import Intro from './Intro.vue'
import Events from './events/Events.vue'
import Speakers from './contacts/Speakers.vue'
import Partners from './contacts/Partners.vue'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Woot woot, I edited!'
    }
  },
    components: {
        Topblock,
        Intro,
        Events,
        Speakers,
        Partners
}
}
</script>

<style lang="scss">
 @import "style/settings.scss";

    .topblock{
  text-align: left;
}
body {
    margin:0px;
#app {
  font-family: $font-stack;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: $primary-color;
  margin-top: 0px;
  width: 100%;
  //margin-left: -10px;
  //margin-right: -10px;


    .newsletter {
        margin-top: 0px;
        width: inherit;
//        margin-left: -10px;
//        margin-right: -10px;
        text-align: center;
    }
}
    }
</style>


<custom1>
    Old stuff from template
    <img src="./assets/logo.png">
    <Message></Message>
    <h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://gitter.im/vuejs/vue" target="_blank">Gitter Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>

</custom1>
