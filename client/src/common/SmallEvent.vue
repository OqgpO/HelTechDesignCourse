<template>
  <div v-if="event" class="main-event-column">
<div class="image-wrapper">
<router-link v-if="event" v-bind:to="eventUri()"><img v-bind:src="event.cover_uri" v-bind:alt="event.title"></router-link>
</div>
<div class="events-title">
<h2><router-link v-bind:to="eventUri()">{{event.title | truncate(30, '')}}</router-link></h2>
</div>
<p>{{event.description | truncate(177, '...')}}</p>
</div>
</template>

<script>
    export default {
        props: ['event'],
        data() {
            return {
                event: this.event,
            }
        },
        methods: {
            eventUri: function() {
                var ret = "event/"
                if (this.event) {
                    return ret + this.event.id
                } else {
                    return ret
                }
            },
        }
    }

</script>



<custom1>
    This could be e.g. documentation for the component.
</custom1>
