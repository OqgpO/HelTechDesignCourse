import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
Vue.use(VueResource);
import router from './router'

var truncate = function (text, length, clamp) {
    clamp = clamp || '...';
    var node = document.createElement('div');
    node.innerHTML = text;
    var content = node.textContent;
    return content.length > length ? content.slice(0, length) + clamp : content;
}

var getDate = function (text) {
    var d = new Date(text);
    return d.toLocaleDateString("en-US", {
        month: 'long',
        day: 'numeric'
    })
}

var getTime = function (text) {
    var d = new Date(text)
    var h = d.getHours()
    var m = d.getMinutes()
    var ret = ""
    if (h < 10) {
        ret = "0" + h
    } else {
        ret = h.toString
    }
    ret += ":"
    if (m < 10) {
        ret += 0;
        ret += m;
    }
    return ret;
}

Vue.filter('getTime', getTime);
Vue.filter('getDate', getDate);
Vue.filter('truncate', truncate);


new Vue({
    el: '#app',
    router,
    template: '<App/>',
    components: {
        App
    }
    //render: h => h(App)
})
