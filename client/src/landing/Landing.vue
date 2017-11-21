<template>
 <div>
<header class="header" id="header">
<div class="headerwrapper">

<Navigation></Navigation>
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
    import Navigation from '../common/Navigation.vue'
    import TopRegion from './TopRegion.vue'
    import Intro from './Intro.vue'
    import EventBlock from './EventBlock.vue'
    import SpeakersPartnersBlock from './SpeakersPartnersBlock.vue'
    import BottomRegion from './BottomRegion.vue'

    export default {
        name: 'Landing',
        components: {
            Navigation,
            TopRegion,
            Intro,
            EventBlock,
            SpeakersPartnersBlock,
            BottomRegion,
        }
    }

</script>

