<template>
<div id="navigation">
<nav id="main-menu" class="responsive-menus-sidr-processed">
<ul class="nice-menu" id="nice-menu">
<li class="menu__item">
<router-link to="/about" title="about" class="menu__link">about</router-link>
</li>
<li class="menu__item">
<router-link to="/events" title="events" class="menu__link">events</router-link>

</li>
<li class="menu__item">
<router-link to="/join" title="join" class="menu__link">join</router-link>
</li>
</ul>
</nav>
</div>
</template>

<script>
   export default {
        props: ['relPath'],
        data() {
            return {
                event: this.relPath,
            }
        },
       methods: {
           getAbs: function(link) {
               var result = link;
               console.log('getting path of: ' + link);
               return result;
           }
    },
   }



</script>
