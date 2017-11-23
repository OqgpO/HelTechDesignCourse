<template>
<div>

<header class="header" id="header">
<div class="headerwrapper">
<div id="logo-wrapper">
<router-link to="./" title="Main page" class="header__logo" id="logo">
<img src="../img/logo.png" alt="Main page" class="header__logo-image" />
</router-link>
</div>

<Navigation></Navigation>

</div>
</header>

<div id="page-events" class="page">
<div id="main">
<div id="content">

<h1>Feeding your curiosity</h1>

<div class="events-text">
<p>In our world of fast developing technology, curiosity is never ending. The thirst for discovery can never be quenched.
For better or worse curiosity drives the world forward. Therefore we wish to plant the seeds of curiosity in people.
We want to achieve this by discovering a different emerging technology topic each month.</p>
</div>

<div id="upcomming-events"> <!--vue.js time!-->
<h2 class="big">Upcoming Events</h2>
<div class="up-events">

<SmallEvent v-for="(event, index) in future" v-bind:key="event.id" v-bind:class="getEventClass(index)" v-bind:event="event"></SmallEvent>
    </div>
    </div>
<div id="past-events"> <!--vue.js time!-->
<h2 class="big">Past Events</h2>
<div class="pt-events">

<SmallEvent v-for="(event, index) in past" :key="event.id" v-bind:class="getEventClass(index)" v-bind:event="event"></SmallEvent>
    </div>
    </div>
    </div>
    </div>
    </div>
<div id="events-bottom-region">	
<BottomRegion></BottomRegion>
</div>
</div>
</template>


<script>
    import BottomRegion from '../landing/BottomRegion.vue'
    import Navigation from '../common/Navigation.vue'
    import SmallEvent from '../common/SmallEvent.vue'

    export default {
        name: 'Events',
        future: [],
        past: [],
        data: function() {
            return {
                past: this.pastEvents ? this.pastEvents : [],
                future: this.future ? this.future : []
            }
        },
        components: {
            BottomRegion,
            Navigation,
            SmallEvent,
        },
        created: function() {
            // `this` points to the vm instance
            this.$http.get('/heltech/api/events/past/9').then(function(response) {
                if (response.ok) {
                    this.past = response.data;
                } else {
                    this.past = [];
                }
            }).catch(function(err) {
                console.log('/heltech/api/events/past/9 unavailable\n' + err);
                this.past = [];
            });
            this.$http.get('/heltech/api/events/future/9').then(function(response) {
                if (response.ok) {
                    this.future = response.data;
                } else {
                    this.future = [];
                }
            }).catch(function(err) {
                this.future = [];
            });
        },
        methods: {
            getEventClass: function(id) {
                return "events-column event-" + (id+1);
            }
        }
    }

</script>
