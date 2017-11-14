<template>
<div id="events-block" class="landing"> <!-- Time for vue.js code -->
<div class="wrapper-events-block">
<div class="main-event events-block-1">
<h1>Ready to<br/>get inspired?</h1>
<div class="image-wrapper">
<a href="event.html"><img v-bind:src="current.cover_uri" v-bind:alt="current.title"></a>
</div>
<div class="text-wrapper">
<h2><a href="event.html">{{current.title}}</a></h2>
<p>{{current.description | truncate 300 }}</p>
<div class="button-wrapper">
<a id="get-tickets-events" class="violet-button" href="#webform-contact" title="Get tickets">get tickets</a>
<a id="all-events" class="violet-button" href="/events.html" title="All events">all events</a>
</div>
</div>
</div>

<div class="other-event events-block-2">
<SmallEvent class="event-1" v-for="event in events" :key="event.id" v-bind:event="event"></SmallEvent>
</div>
</div>
</div>
</template>

<script>
    import SmallEvent from './common/SmallEvent.vue'

    export default {
        data() {
            return {
                events: this.events,
                current: this.current,
            }
        },

        created: function() {
            // `this` points to the vm instance
            this.$http.get('/heltech/api/events/past/2').then(function(response) {
                console.log(response.data);
                this.events = response.data;
            });
            this.$http.get('/heltech/api/events/current').then(function(response) {
                console.log(response.data);
                this.current = response.data;
            });
            console.log('a is: ' + this.events)
        },

        ready: function() {

        },

        components: {
            SmallEvent,
        }
    }

</script>

<style>


</style>

<custom1>
</custom1>
