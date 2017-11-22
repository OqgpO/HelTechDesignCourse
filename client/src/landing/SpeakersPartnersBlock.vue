<template>
<div class="speakers-partners-block">
<div id="speakers-block" class="landing">
<h1>Previous Speakers</h1> <!-- http://kenwheeler.github.io/slick/#getting-started -->
<div class="speakers-wrapper">
<div class="speaker speaker-1">

<div class="image-wrapper">
<img src="../img/speaker.jpeg" alt="Kimmo Tiikikainen">
</div>
<div class="speakers-title">
<h4>Kimmo Tiikikainen</h4>
</div>
<p>Finnish Minister of Housing, Energy and the Environment </p>
</div>

<div class="speaker speaker-2">

<div class="image-wrapper">
<img src="../img/speaker.jpeg" alt="Julian Hosp">
</div>
<div class="speakers-title">
<h4>Julian Hosp</h4>
</div>
<p>President at Tenx</p>

</div>
<div class="speaker speaker-3">

<div class="image-wrapper">
<img src="../img/speaker.jpeg" alt="Peter Vesterbacka">
</div>
<div class="speakers-title">
<h4>Peter Vesterbacka</h4>
</div>
<p>Co-founder of Lightneer Inc</p>

</div>
<div class="speaker speaker-4">

<div class="image-wrapper">
<img src="../img/speaker.jpeg" alt="Heli Antila">
</div>
<div class="speakers-title">
<h4>Heli Antila</h4>
</div>
<p>CTO at Fortum</p>

</div>
<div class="speaker speaker-5">

<div class="image-wrapper">
<img src="../img/speaker.jpeg" alt="Mikko Honkanen">
</div>
<div class="speakers-title">
<h4>Mikko Honkanen</h4>
</div>
<p>CEO at Vainu.io</p>

</div>
<div class="speaker speaker-6">

<div class="image-wrapper">
<img src="../img/speaker.jpeg" alt="Ilkka Kivimäki">
</div>
<div class="speakers-title">
<h4>Ilkka Kivimäki</h4>
</div>
<p>Partner at Inventure</p>

</div>
<div class="speaker speaker-7">

<div class="image-wrapper">
<img src="../img/speaker.jpeg" alt="Tuomas Tikka">
</div>
<div class="speakers-title">
<h4>Tuomas Tikka</h4>
</div>
<p>CEO at Space Lab Reaktor</p>

</div>
<div class="speaker speaker-8">

<div class="image-wrapper">
<img src="../img/speaker.jpeg" alt="Tuomas Tikka">
</div>
<div class="speakers-title">
<h4>Marika Kukkasniemi</h4>
</div>
<p>CEO & Co founder of Kokoa Agency</p>

</div>
</div>
</div>

<div id="partners-block" class="landing">
<h1>Our Partners</h1>
<div class="partners-logos">
<div class="image-wrapper">
<div>
<img src="../img/partners-nasdaq.png" alt="Nasdaq">
</div>
<div>
<img src="../img/partners-ey.png" alt="EY">
</div>
<div>
<img src="../img/partners-ms.png" alt="MS">
</div>
</div>
<p> Do you want to enable the Finnish Tech scene with us? Contact us at teodora.berg@aaltoes.com</p>
</div>

</div>
</div>

</template>


<script>
    import Speaker from '../common/Speaker.vue'

    export default {
        data() {
            return {
                msg: 'Speakers block'
            }
        },
        components: {
            Speaker,
        }
    }

</script>


<style></style>
