<template>
  <article class="media post has-background-light">
  <figure class="media-left">
    <router-link :to="{name: 'profile', params: {username: post.author.username}}">
      <p class="image is-64x64">
        <img class="is-rounded" :src="'/static/social/img/profile_default.jpeg'">
      </p>
    </router-link>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <router-link :to="{name: 'profile', params: {username: post.author.username}}">
          <strong>{{ post.author.profile.display_name }}</strong> <small>@{{ post.author.username }}</small> 
        </router-link> <small>{{ post.created | formatDateTime }}</small>
        <br>
        {{ post.text }}
      </p>
    </div>
    <nav class="level is-mobile">
      <div class="level-left">
        <a class="level-item">
          <span class="icon is-small"><i class="fas fa-reply"></i></span>
        </a>
        <a class="level-item" v-on:click="toggleLike">

          <span v-bind:class="{'has-text-danger': post.liked}" class="icon is-small"><i class="fas fa-heart"></i></span>
        </a>
      </div>
    </nav>
  </div>
</article>
</template>

<script>

export default {
  name: 'Post',
  components: {

  },
  props: {
    post: Object,
  },
  created(){
    
  },
  methods: {
    toggleLike(){
      fetch("/api/posts/"+this.post.id+"/like/", {
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
        if(result.liked){
          this.post.liked = true;
        } else {
          this.post.liked = false;
        }
      }).catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.post {
  margin: 1rem 0;
  padding: 1rem;
  border-radius: 10px;
}
</style>
