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

<div v-if="event" id="page-event" class="page">
<div id="main">
<div id="content">
<div class="event image-wrapper">
<img v-bind:src="event.cover_uri" v-bind:alt="event.cover_uri">
</div>
<div class="event description">
<h1>{{event.title}}</h1>
<h5>{{event.punchline}}</h5>
<p>{{event.description}}</p>
</div>

<div class="event first-line">
<div class="column-one">
<h5>keynote</h5>
<p v-for="kn in keynote" :key="kn.event"><b>{{kn.full_name}}</b>,<br/>{{kn.title}}</p>
</div>
<div class="column-two">
<h5>Panel</h5>
<p v-for="pan in panel" :key="pan.event"><b>{{pan.full_name}}</b>,<br/>{{pan.title}}</p>
</div>
<div class="column-three">
<h5>Demo startups</h5>
    <p v-for="person in demo" :key="person.event"><b><i>{{person.organisation.name}}</i></b></p>
</div>
</div>

<div class="event second-line">
<div class="column-one">
<h5>Date</h5>
<p>{{event.start_time | getDate }}</p>
</div>
<div class="column-two">
<h5>Time</h5>
<p>{{event.start_time | getTime }}</p>
</div>
<div class="column-three">
<h5>Location</h5>
<p>{{event.place.name}},<br/> {{event.place.streetaddr}} </p>
</div>
</div>

<a v-if="upcoming" class="black-button event-button" href="https://holvi.com/shop/aaltoes16/section/hel-tech-meetup/" title="Tickets">Get tickets</a>
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
        keynote: [],
        panel: [],
        demo: [],
        event: {},
        upcoming: false,
        components: {
            BottomRegion,
            Navigation,
        },
        data() {
            return {
                event: this.event,
                keynote: this.keynote,
                panel: this.panel,
                demo: this.demo,
                upcoming: this.upcoming
            }
        },
        created: function() {
            this.eventId = this.$route.params.id
            // `this` points to the vm instance
            this.$http.get('/api/events/' + this.eventId).then(function(response) {
                this.event = response.data;
                var e_time = new Date(this.event.start_time)
                this.upcoming = e_time > Date.now()
            }).catch(function(err) {
                console.log('/api/events/' + this.eventId + ' unavailable');
                this.event = {}
            });

            this.$http.get('/api/events/' + this.eventId + "/keynote").then(function(response) {
                this.keynote = response.data;
            }).catch(function(err) {
                console.log('/api/events/' + this.eventId + '/keynote unavailable');
                this.keynote = {}
            });

            this.$http.get('/api/events/' + this.eventId + "/panel").then(function(response) {
                this.panel = response.data;
            }).catch(function(err) {
                console.log('/api/events/' + this.eventId + '/panel unavailable');
                this.panel = {}
            });


            this.$http.get('/api/events/' + this.eventId + "/demo").then(function(response) {
                this.demo = response.data;
            }).catch(function(err) {
                console.log('/api/events/' + this.eventId + '/demo unavailable');
                this.demo = {}
            });
        },
    }

</script>



<custom1>
    This could be e.g. documentation for the component.
</custom1>
