<template>
  <div>
<header class="header" id="header">
<div class="headerwrapper">
<div id="logo-wrapper">
<router-link to="/" title="Main page" class="header__logo" id="logo">
<img src="../img/logo.png" alt="Main page" class="header__logo-image" />
</router-link>
</div>

 <Navigation></Navigation>

</div>
</header>

<div id="page-event" class="page">
<div id="main">
<div id="content">
<div class="event image-wrapper">
<img v-bind:src="event.cover_page || 'Event Not found'" v-bind:alt="event.cover_page">
</div>
<div class="event description">
<h1>{{event.title}}</h1>
<h5>{{event.punchline}}</h5>
<p>{{event.description}}</p>
</div>

<div class="event first-line">
<div class="column-one">
<h5>keynote</h5>
<p><b>Elias Poyry</b>,<br/>Chief Business Officer of Virta Ltd</p>
</div>
<div class="column-two">
<h5>Panel</h5>
<p><b>Elias Poyry</b>,<br/>Chief Business Officer of Virta Ltd</p>
<p><b>Elias Poyry</b>,<br/>Chief Business Officer of Virta Ltd</p>
<p><b>Elias Poyry</b>,<br/>Chief Business Officer of Virta Ltd</p>
</div>
<div class="column-three">
<h5>Demo startups</h5>
<p>Teraloop</p>
<p>Teraloop</p>
<p>Teraloop</p>
</div>
</div>

<div class="event second-line">
<div class="column-one">
<h5>Date</h5>
<p>November 6th</p>
</div>
<div class="column-two">
<h5>Time</h5>
<p>18:00</p>
</div>
<div class="column-three">
<h5>Location</h5>
<p>Valkoinen Sali</p>
</div>
</div>

<a class="black-button event-button" href="/" title="test button">Get tickets</a>
</div>
</div>
</div>

<BottomRegion></BottomRegion>


</div>
</template>

<script>
    import BottomRegion from '../landing/BottomRegion.vue'
    import Navigation from '../common/Navigation.vue'

    export default {
        name: 'EventDetail',
        eventId: "",
        event: {},
        components: {
            BottomRegion,
            Navigation,
        },
        data() {
            return {
                event: this.event,
            }
        },
        created: function() {
            this.eventId = this.$route.params.id
            // `this` points to the vm instance
            this.$http.get('/heltech/api/events/' + this.eventId).then(function(response) {
                console.log(response.data);
                this.event = response.data;
            }).catch(function(err) {
                console.log('/heltech/api/events/' + this.eventId + ' unavailable');
                this.event = {}
            });
        },
    }

</script>



<custom1>
    This could be e.g. documentation for the component.
</custom1>
