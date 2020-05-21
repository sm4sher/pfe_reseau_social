<template>
<nav class="navbar is-dark" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="/home">
      <!--<img src="" width="112" height="28">-->
      Social network
    </a>

    <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-start">
      <a href="/home" class="navbar-item">
        Home
      </a>

      <a class="navbar-item">
        Profil
      </a>

      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          Item2
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            Item
          </a>
          <a class="navbar-item">
            Item
          </a>
          <a class="navbar-item">
            Item
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item">
            Item
          </a>
        </div>
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
          <a class="button is-light">
            Log in
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>

<script>

export default {
  name: 'NavBar',
}
</script>

<style scoped>

</style>