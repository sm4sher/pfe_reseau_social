<template>
  <div id="app">
    <header>
      <nav-bar></nav-bar>
    </header>

    <main class="section has-background-grey-dark">
      <div class="container">
        <router-view :key="$route.fullPath"></router-view>
      </div>
    </main>

    <footer class="footer has-background-grey-dark has-text-white">
      <div class="content has-text-centered">
        <p>Social Network by Adrien</p>
      </div>
    </footer>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar,
  },
}
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
main {
  flex: 1;
}
a:active, a:focus {
  outline: none;
  -moz-outline-style: none;
}
</style>
