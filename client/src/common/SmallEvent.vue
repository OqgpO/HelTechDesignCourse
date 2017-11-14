<template>
  <div class="main-event-column">
<div class="image-wrapper">
<a href="event.html"><img v-bind:src="event.cover_uri" v-bind:alt="event.title"></a>
</div>
<div class="events-title">
<h2><a href="event.html">{{event.title}}</a></h2>
</div>
<p>{{event.description | truncate(200, '...')}}</p>
</div>

</template>

<script>
    export default {
        props: ['event'],
        data() {
            return {
                event: this.event,
            }
        }
    }

</script>



<custom1>
    This could be e.g. documentation for the component.
</custom1>
