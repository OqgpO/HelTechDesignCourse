<template>
<div class="region region-top main">
<div id="top-block" class="landing">
<div id="main-logo">
</div>
<div class="button-wrapper">
<a id="get-tickets-main" class="black-button" href="https://holvi.com/shop/aaltoes16/section/hel-tech-meetup/" title="Get tickets">get tickets</a>
<router-link id="join-main" class="black-button" to="join" title="Get on stage">{{msg}}</router-link>
</div>
</div>
</div>
</template>

<script>
    export default {
        data() {
            return {
                msg: 'Get on stage'
            }
        }
    }

</script>

<style>


</style>
