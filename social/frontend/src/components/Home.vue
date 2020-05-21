<template>
  <div>
    <h1>Home</h1>
    <new-post></new-post>
    <div v-for="post in posts" :key="post.id">
      <post :post="post"></post>
    </div>
  </div>
</template>

<script>
import Post from './Post.vue'
import NewPost from './NewPost.vue'

export default {
  name: 'Home',
  components: {
    Post,
    NewPost
  },
  data(){
    return {
      posts: Array,
    }
  },
  mounted(){
    //Fetch posts
    console.log(this);
    fetch("/api/posts/").then(function (response) {
            return response.json();
    }).then((result) => {
        this.posts = result;
    }).catch((err) => { 
        alert(err); 
    });
  },
}
</script>

<style scoped>

</style>
