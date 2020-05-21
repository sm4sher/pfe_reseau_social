<template>
  <div id="app">
    <header><nav-bar></nav-bar></header>
    <main class="container">
      <!--<timeline :timeline="this.$store.state.user.timeline"></timeline>-->
      <router-view></router-view>
    </main>
    <footer class="footer"><div class="content has-text-centered"><p>Social Network by Adrien</p></div></footer>
  </div>
</template>

<script>
//import Timeline from './components/Timeline.vue'
import NavBar from './components/NavBar.vue'
export default {
  name: 'App',
  components: {
    //Timeline,
    NavBar,
  },
}
</script>

<style>

</style>
