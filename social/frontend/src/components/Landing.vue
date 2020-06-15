<template>
  <div class="hero is-dark has-background-grey-dark">
    <div class="hero-body landing-hero">
      <div class="container">
        <h1 class="title">Social Network</h1>
        <h2 class="subtitle">Login or create an account now</h2>
        <div class="columns landing-buttons buttons">
          <router-link class="button is-primary" :to="{name: 'register'}">Register</router-link>
          <router-link class="button" :to="{name: 'login'}">Login</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Landing',
  components: {

  },
  mounted(){
    if(this.$store.state.user != null){
      this.$router.push('home')
    }
  }
}
</script>

<style>
.landing-buttons {
  margin: 4rem 4rem;
}
</style>
