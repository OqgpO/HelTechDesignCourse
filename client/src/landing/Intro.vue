<template>
  <div id="desc-block" class="landing">
<div class="desc-block image-wrapper">
<img src="../img/main-about-background.jpg" alt="About HelTech">
</div>
<div class="desc-block wrapper">
<h1>{{titlepre}}<br/>{{titlepost}}</h1>
<p>{{introtext}}</p>
</div>
</div>
</template>

<script>
    export default {
        data() {
            return {
                titlepre: "Helsinki's",
                titlepost: "tech meetup",
                introtext: "Every first Monday night of each month we gather the Finnish tech scene, with foreign visitors in the centre of Helsinki.\n The purpose of the event is to educate, inspire and finally to connect tech enthusiasts, by discussing the latest trends in technology with the help of interesting participants and company representatives."
            }
        }
    }

</script>



<custom1>
    This could be e.g. documentation for the component.
</custom1>
