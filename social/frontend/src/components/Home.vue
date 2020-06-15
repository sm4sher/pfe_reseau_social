<template>
  <div>
    <h2 class="title is-2 has-text-white">Home</h2>
    <new-post v-on:new-post="addPost"></new-post>
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
    fetch("/api/posts/").then(function (response) {
            return response.json();
    }).then((result) => {
        this.posts = result.reverse();
    }).catch((err) => { 
        alert(err); 
    });
  },
  methods: {
    addPost(post){
      this.posts.unshift(post);
    }
  }

}
</script>

<style>

</style>
