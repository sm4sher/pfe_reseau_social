<template>
  <div class="post">
    <p>{{ post.text }}</p>
  </div>
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
