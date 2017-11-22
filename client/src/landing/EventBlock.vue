<template>
<div id="events-block" class="landing"> <!-- Time for vue.js code -->
<div class="wrapper-events-block">
<div class="main-event events-block-1">
<h1>Ready to<br/>get inspired?</h1>
<div class="image-wrapper">
<router-link v-bind:to="eventUri()"><img v-bind:src="current.cover_uri || 'Not Found' " v-bind:alt="current.title || 'Not Found' "></router-link>
</div>
<div class="text-wrapper">
<h2><router-link v-bind:to="eventUri()">{{current.title || "Not Found" }}</router-link></h2>
<p>{{current.description | truncate(300) || "Not Found" }}</p>
<div class="button-wrapper">
<a id="get-tickets-events" class="violet-button" href="#webform-contact" title="Get tickets">get tickets</a>
<router-link id="all-events" class="violet-button" to="events" title="All events">all events</router-link>
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
    import SmallEvent from '../common/SmallEvent.vue'

    export default {
        data() {
            return {
                events: this.events ? this.events : [],
                current: this.current ? this.current : {},
            }
        },

        created: function() {
            // `this` points to the vm instance
            this.$http.get('/heltech/api/events/past/2').then(function(response) {
                if (response.ok) {
                    console.log(response.data);
                    this.events = response.data;
                } else {
                    this.events = [];
                }
            }).catch(function(err){
                console.log('/heltech/api/events/past/2 unavailable\n' + err);
                this.events = [];
            });
            this.$http.get('/heltech/api/events/current').then(function(response) {
                if (response.ok) {
                    console.log(response.data);
                    this.current = response.data;
                } else {
                    this.current = {};
                }
            }).catch(function(err){
                console.log('/heltech/api/events/current unavailable' + err);
                this.current = {};
            });
        },

        ready: function() {

        },

        components: {
            SmallEvent,
        },
        methods: {
            eventUri: function() {
                var ret = "event/"
                if (this.current) {
                    return ret
                } else {
                    return ret + this.current.id
                }
            },
        }
    }

</script>

<style>


</style>

<custom1>
</custom1>
