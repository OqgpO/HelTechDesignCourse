import Vue from 'vue'
import Router from 'vue-router'
import Landing from '../landing/Landing.vue'
//import AllEvents from '../events/Events.vue'
import EventDetail from '../event/Event.vue'
import About from '../about/About.vue'
import Join from '../join/Join.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.ROUTER_BASE,
    routes: [
        {
            path: '/',
            name: 'Landing',
            component: Landing
    },
        {
            path: '/about',
            name: 'About',
            component: About
    },
        /*{
            path: '/events',
            name: 'AllEvents',
            component: AllEvents
    },*/
        {
            path: '/event/:id',
            name: 'EventDetail',
            component: EventDetail
    },
        {
            path: '/join',
            name: 'Join',
            component: Join
    }
    ]
})
