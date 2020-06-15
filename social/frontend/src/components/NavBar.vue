<template>
<nav class="navbar is-dark" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <router-link class="navbar-item" :to="{path: '/'}">
      <!--<img src="" width="112" height="28">-->
      Social network
    </router-link>

    <a role="button" id="navbar-burger" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbar">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbar" class="navbar-menu">
    <div class="navbar-start">
      <router-link class="navbar-item" :to="{path: '/'}">Home</router-link>
      <router-link v-if="$store.getters.islogged" class="navbar-item" :to="{name: 'profile', params: {username: $store.state.user.username}}">Profile</router-link>
    </div>

    <div class="navbar-end">
      <div v-if="$store.getters.islogged" class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link is-vcentered is-centered is-mobile">
          <div class="column is-4">
            <p class="image is-24x24">
              <img class="is-rounded" :src="'/static/social/img/'+$store.state.user.profile.picture">
            </p>
          </div>
          <p class="column is-8">
            {{ $store.state.user.profile.display_name }}
          </p>
        </a>
        <div class="navbar-dropdown">
          <a class="navbar-item">
            Profile
          </a>
          <a class="navbar-item">
            Settings
          </a>
          <hr class="navbar-divider">
          <a v-on:click="logout" class="navbar-item">
            Logout
          </a>
        </div>
      </div>
      <div v-else class="navbar-item">
        <div class="buttons">
          <router-link class="button is-primary" :to="{name: 'register'}">
            <strong>Sign up</strong>
          </router-link>
          <router-link class="button is-light" :to="{name: 'login'}">
            Log in
          </router-link>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>

<script>

export default {
  name: 'NavBar',
  methods: {
    logout(){
      fetch("/api/logout/").then((response) => {
        if(response.status == 200){
          this.$store.commit('logout');
          this.$router.push('/')
        }
      })
    }
  },
  mounted(){
    // to expand navbar on small screens
    var burger = document.getElementById("navbar-burger");
    burger.addEventListener('click', () => {
      const target = burger.dataset.target;
      const $target = document.getElementById(target);
      burger.classList.toggle('is-active');
      $target.classList.toggle('is-active');
    });
  }
}
</script>

<style>
.profile-item {
  margin-right: 1rem;
  margin-bottom: 0;
}
.logout-button {
  margin: 0 2rem;
}
</style>