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

<p>In our world of fast developing technology, curiosity is never ending. The thirst for discovery can never be quenched.
For better or worse curiosity drives the world forward. Therefore we wish to plant the seeds of curiosity in people.
We want to achieve this by discovering a different emerging technology topic each month.</p>


<div id="upcomming-events"> <!--vue.js time!-->
<h2>Upcoming Events</h2>
<div class="up-events">

<SmallEvent v-for="event in future" v-bind:key="event.id" class="events-column event-1" v-bind:event="event"></SmallEvent>
    </div>
    </div>
<div id="past-events"> <!--vue.js time!-->
<h2>Past Events</h2>
<div class="pt-events">

<ul>
<li v-for="item in future" :key="item.id">{{item.name}}</li>
</ul>

<SmallEvent v-for="event in past" :key="event.id" v-bind:class="getEventClass(event.id)" v-bind:event="event"></SmallEvent>
    </div>
    </div>
    </div>
    </div>
    </div>
<BottomRegion></BottomRegion>

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
                    console.log('/heltech/api/events/past/9' + response.data);
                    this.pastEvents = response.data;
                } else {
                    this.pastEvents = [];
                }
            }).catch(function(err) {
                console.log('/heltech/api/events/past/9 unavailable\n' + err);
                this.pastEvents = [];
            });
            this.$http.get('/heltech/api/events/future/9').then(function(response) {
                if (response.ok) {
                    console.log('/heltech/api/events/future/9' + response.data);
                    this.current = response.data;
                } else {
                    this.future = [];
                }
            }).catch(function(err) {
                console.log('/heltech/api/events/future/9 unavailable' + err);
                this.future = [];
            });
        },
        methods: {
            getEventClass: function(id) {
                console.log("events-column event-" + id)
                return "events-column event-" + id;
            }
        }
    }

</script>
