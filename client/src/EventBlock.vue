<template>
<div id="events-block" class="landing"> <!-- Time for vue.js code -->
<div class="wrapper-events-block">
<div class="main-event events-block-1">
<h1>Ready to<br/>get inspired?</h1>
<div class="image-wrapper">
<a href="event.html"><img src='./img/nature-forest.jpeg' alt="Pines"></a>
</div>
<div class="text-wrapper">
<h2><a href="event.html">Smart Grid</a></h2>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
<div class="button-wrapper">
<a id="get-tickets-events" class="violet-button" href="#webform-contact" title="Get tickets">get tickets</a>
<a id="all-events" class="violet-button" href="/events.html" title="All events">all events</a>
</div>
</div>
</div>

<div class="other-event events-block-2" vue-for:="event in past-events">

<SmallEvent class="event-1"></SmallEvent>
<SmallEvent class="event-2"></SmallEvent>

</div>
</div>
</div>
</template>

<script>
    //import Currentevent from './Currentevent.vue'
    import SmallEvent from './common/SmallEvent.vue'

    export default {
        data() {
            return {
                msg: 'Events block'
            }
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
