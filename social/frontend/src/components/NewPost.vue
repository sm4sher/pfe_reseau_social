<template>
  <article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img :src="$store.state.user.profile.picture">
    </p>
  </figure>
  <div class="media-content">
    <div class="field">
      <p class="control">
        <textarea class="textarea" placeholder="Add a post..."></textarea>
      </p>
    </div>
    <nav class="level">
      <div class="level-left">
        <div class="level-item">
          <a class="button is-info">Submit</a>
        </div>
      </div>
    </nav>
  </div>
</article>
</template>

<script>

export default {
  name: 'NewPost',
  components: {

  },
  created(){
    
  }
}
</script>

<style scoped>

</style>
