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

<div class="events-column event-1">
<div class="image-wrapper">
<a href="event.html"><img src="img/neurocells.jpg" alt="Neurocells"></a>
</div>
<div class="events-title">
<h2><a href="event.html">Smart Grid</a></h2>
</div>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
</div>

<div class="events-column event-2">
<div class="image-wrapper">
<a href="event.html"><img src="img/industry.jpg" alt="Industry"></a>
</div>
<div class="events-title">
<h2><a href="event.html">100 years of finnish tech</a></h2>
</div>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>

<div class="events-column event-3">
<div class="image-wrapper">
<a href="event.html"><img src="img/industry.jpg" alt="Industry"></a>
</div>
<div class="events-title">
<h2><a href="event.html">100 years of finnish tech</a></h2>
</div>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>

</div>
</div>

<div id="past-events"> <!--vue.js time!-->
<h2>Past Events</h2>
<div class="pt-events">

<div class="events-column event-1">
<div class="image-wrapper">
<a href="event.html"><img src="img/neurocells.jpg" alt="Neurocells"></a>
</div>
<div class="events-title">
<h2><a href="event.html">Smart Grid</a></h2>
</div>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
</div>

<div class="events-column event-2">
<div class="image-wrapper">
<a href="event.html"><img src="img/industry.jpg" alt="Industry"></a>
</div>
<div class="events-title">
<h2><a href="event.html">100 years of finnish tech</a></h2>
</div>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>

<div class="events-column event-3">
<div class="image-wrapper">
<a href="event.html"><img src="img/industry.jpg" alt="Industry"></a>
</div>
<div class="events-title">
<h2><a href="event.html">100 years of finnish tech</a></h2>
</div>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>

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

    export default {
        name: 'Events',
        components: {
            BottomRegion,
            Navigation,
        },
        created: function() {
            // `this` points to the vm instance
            this.$http.get('/heltech/api/events/past/9').then(function(response) {
                if (response.ok) {
                    console.log(response.data);
                    this.events = response.data;
                } else {
                    this.events = [];
                }
            }).catch(function(err) {
                console.log('/heltech/api/events/past/9 unavailable\n' + err);
                this.events = [];
            });
            this.$http.get('/heltech/api/events/current').then(function(response) {
                if (response.ok) {
                    console.log(response.data);
                    this.current = response.data;
                } else {
                    this.current = {};
                }
            }).catch(function(err) {
                console.log('/heltech/api/events/current unavailable' + err);
                this.current = {};
            });
        },
    }

</script>
