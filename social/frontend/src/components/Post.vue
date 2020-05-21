<template>
  <article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img :src="'/static/social/img/profile_default.jpeg'">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <p>
        <strong>{{ post.author.profile.display_name }}</strong> <small>@{{ post.author.username }}</small> <small>{{ post.created | formatDateTime }}</small>
        <br>
        {{ post.text }}
      </p>
    </div>
    <nav class="level is-mobile">
      <div class="level-left">
        <a class="level-item">
          <span class="icon is-small"><i class="fas fa-reply"></i></span>
        </a>
        <a class="level-item">
          <span class="icon is-small"><i class="fas fa-retweet"></i></span>
        </a>
        <a class="level-item">
          <span class="icon is-small"><i class="fas fa-heart"></i></span>
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
    
  }
}
</script>

<style scoped>

</style>
