<template>
  <div id="app">
    <header>Header</header>
    <main>
      <timeline :timeline="this.$store.state.user.timeline"></timeline>
    </main>
    <footer>Footer</footer>
  </div>
</template>

<script>
import Timeline from './components/Timeline.vue'

export default {
  name: 'App',
  components: {
    Timeline
  },
}
</script>

<style>

</style>
