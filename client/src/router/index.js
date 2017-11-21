import Vue from 'vue'
import Router from 'vue-router'
import Landing from '../landing/Landing.vue'
    //import Events from '../events/Events.vue'
    //import Event from '../event/Event.vue'
import About from '../about/About.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/client/',
            name: 'Landing',
            component: Landing
    },
        {
            path: '/client/about/',
            name: 'About',
            component: About
    },
/*        {
            path: '/events/',
            name: 'Events',
            component: Events
    },
        {
            path: '/event/:id',
            name: 'Event',
            component: Event
    },*/
  ]
})
