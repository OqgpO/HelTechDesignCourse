<template>
 <div>
<header class="header" id="header">
<div class="headerwrapper">
<div id="navigation">
<nav id="main-menu" class="responsive-menus-sidr-processed">
<ul class="nice-menu" id="nice-menu">
<li class="menu__item">
<router-link to="./about/" title="about" class="menu__link">about</router-link>
</li>
<li class="menu__item">
<router-link to="./events/" title="events" class="menu__link">events</router-link>
</li>
<li class="menu__item">
<router-link to="./join/" title="join" class="menu__link">join</router-link>
</li>
</ul>
</nav>
</div>
</div>
</header>

    <TopRegion></TopRegion>
  <div id="page-main" class="page">
<div id="main">
<div id="content">
<Intro></Intro>
<EventBlock></EventBlock>
<SpeakersPartnersBlock></SpeakersPartnersBlock>
<BottomRegion></BottomRegion>
</div>
</div>

  </div>
  </div>
</template>

<script>
    import TopRegion from './TopRegion.vue'
    import Intro from './Intro.vue'
    import EventBlock from './EventBlock.vue'
    import SpeakersPartnersBlock from './SpeakersPartnersBlock.vue'
    import BottomRegion from './BottomRegion.vue'

    export default {
        name: 'Landing',
        components: {
            TopRegion,
            Intro,
            EventBlock,
            SpeakersPartnersBlock,
            BottomRegion,
        }
    }

</script>

