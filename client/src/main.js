import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import router from './router'

Vue.use(VueResource);

var filter = function (text, length, clamp) {
    clamp = clamp || '...';
    var node = document.createElement('div');
    node.innerHTML = text;
    var content = node.textContent;
    return content.length > length ? content.slice(0, length) + clamp : content;
};

Vue.filter('truncate', filter);

new Vue({
    el: '#app',
    router,
    template: '<App/>',
    components: {
        App
    }
    //render: h => h(App)
})
