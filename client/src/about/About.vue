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

<div id="page-about" class="page">
<div id="main">
<div id="content">
<h1>HELSINIKI'S MEETING POINT <br/>FOR TECH ENTHUSIASTS</h1>
<div id="our-story" class="about center-block">
<p>HEL Tech Meetup is a monthly event with the purpose to educate, inspire and connect tech enthusiasts in Helsinki area and provide
opportunities for the Helsinki tech community and ecosystem to leverage their capabilities and results.</p>
<p>It is hotspot of Helsinki's brightest minds showcasing and discussing the latest technology trends, with the help of engaging
participants and partner company representatives. We bring prominent
names in the Finnish tech scene, as well as foreign visitors under one roof with hackers, entrepreneurs, students, academics,
investors, and designers of Helsinki.</p>
<p>Each event consists of one keynote, panel discussion, news section, demos, pitches by startups, and concludes with
a networking session in a relaxed setting. Furthermore, the event provides technology companies the opportunity to
launch and showcase their new products and services.</p>
</div>

</div>
</div>
</div>

<BottomRegion></BottomRegion>

</div>
</template>




<script>
    import Navigation from '../common/Navigation.vue'
    import BottomRegion from '../landing/BottomRegion.vue'

    export default {
        name: 'About',
        components: {
            BottomRegion,
            Navigation,
        }
    }

</script>


<style>


</style>
