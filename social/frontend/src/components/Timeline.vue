<template>
  <div class="timeline">
    <h1>Timeline</h1>
    <div v-for="post in timeline.posts" :key="post.id">
      <post :post="post"></post>
    </div>
  </div>
</template>

<script>
import Post from './Post.vue'

export default {
  name: 'Timeline',
  components: {
    Post
  },
  props: {
    timeline: Object,
  },
}
</script>

<style scoped>

</style>
