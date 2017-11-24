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

<div id="page-join" class="page">
<div id="main">
<div id="content">
<h1>Want to join?</h1>
<div id="contribute-join" class="join center-block">
<h4>You want to pitch, demo, or even launch your product at Hel Tech?</h4>
<p>Let’s do it! Please fill in the form below. We will get in touch with you asap.<p>
<p>“Big thanks to organizers for the great event, and to everyone attending. It was really a pleasure to see this level event kept in Helsinki, and to see so many people being really interested about the topic. Also thank for letting me share some of my thoughts on the stage!” Bitcoin Entrepreneur, 5.9.2017</p>
</div>

</div>
</div>
</div>

<JoinBottomRegion></JoinBottomRegion>

</div>
</template>


<script>
    import JoinBottomRegion from './JoinBottomRegion.vue'
    import Navigation from '../common/Navigation.vue'

    export default {
        name: 'Join',
        components: {
            JoinBottomRegion,
            Navigation,
        }
    }

</script>
