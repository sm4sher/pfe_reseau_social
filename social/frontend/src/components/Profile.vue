<template>
  <div>
    <div class="profile-head has-background-light">
      <div class="level">
        <div class="level-item has-text-centered">
          <p class="image is-128x128">
            <img class="is-rounded" :src="'/static/social/img/'+user.profile.picture">
          </p>
        </div>
      </div>
      <div class="level">
        <div class="level-item has-text-centered">
          <div>
            <h2 class="title is-2">{{ user.profile.display_name }}</h2>
            <p>@{{ user.username}}</p>
            <p>{{ user.profile.bio }}</p>
            <div v-if="user.id != $store.state.user.id" class="user-actions">
              <button v-if="user.profile.followed" v-on:click="toggleFollow" class="button is-primary">Following</button>
              <button v-else v-on:click="toggleFollow" class="button is-primary is-outlined">Follow</button>

              <button class="button is-link">Send PM</button>
            </div>
            <div v-else class="user-action">
              <button class="button is-link">Edit profile</button>
            </div>
          </div>
        </div>
      </div>
      <nav class="level is-mobile">
        <div class="level-item has-text-centered">
          <router-link :to="{name: 'profile'}">
            <div>
              <p class="heading">Posts</p>
              <p class="title">{{ user.profile.nbposts }}</p>
            </div>
          </router-link>
        </div>
        <div class="level-item has-text-centered">
          <router-link :to="{name: 'profile-following'}">
            <div>
              <p class="heading">Following</p>
              <p class="title">{{ user.profile.nbfollowing }}</p>
            </div>
          </router-link>
        </div>
        <div class="level-item has-text-centered">
          <router-link :to="{name: 'profile-followers'}">
            <div>
              <p class="heading">Followers</p>
              <p class="title">{{ user.profile.nbfollowers }}</p>
            </div>
          </router-link>
        </div>
        <div class="level-item has-text-centered">
          <router-link :to="{name: 'profile-likes'}">
            <div>
              <p class="heading">Likes</p>
              <p class="title">{{ user.profile.nblikes }}</p>
            </div>
          </router-link>
        </div>
      </nav>
    </div>

    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>

<script>

export default {
  name: 'Profile',
  components: {

  },
  data(){
    return {
      user: {profile: Array},
    }
  },
  mounted(){
    //Fetch user
    fetch("/api/users/"+this.$route.params.username+'/').then(function (response) {
            return response.json();
    }).then((result) => {
        this.user = result;
    }).catch((err) => { 
        console.log(err); 
    });
  },
  methods: {
    toggleFollow(){
      fetch("/api/users/"+this.user.username+"/follow/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.getToken(),
        },
      }).then((response) => {
        if(response.status == 200){
          return response.json();
        }
        else {
          throw Error;
        }
      }).then((result) => {
        console.log(result)
        if(result.followed){
          this.user.profile.followed = true;
        } else {
          this.user.profile.followed = false;
        }
      }).catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.profile-head {
  padding: 2rem;
  border-radius: 10px;
}
.user-actions button {
  margin: 1rem 0.5rem;
}
.router-link-exact-active {
  color: blue;
} 
.router-link-exact-active .title {
  color: blue;
}
</style>
