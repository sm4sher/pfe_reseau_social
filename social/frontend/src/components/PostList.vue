<template>
  <div>
    <h2 v-if="title != ''" class="title is-2 has-text-white">{{ title }}</h2>
    <new-post v-if="newpostPrompt" v-on:new-post="addPost"></new-post>
    <div v-for="post in posts" :key="post.id">
      <post :post="post"></post>
    </div>
  </div>
</template>

<script>
import Post from './Post.vue'
import NewPost from './NewPost.vue'

export default {
  name: 'PostList',
  components: {
    Post,
    NewPost
  },
  props: {
    source: String,
    title: String,
    newpostPrompt: Boolean,
  },
  data(){
    return {
      posts: Array,
    }
  },
  mounted(){
    this.loadPosts();
  },
  methods: {
    addPost(post){
      this.posts.unshift(post);
    },
    loadPosts(){
      //Fetch posts TODO: pagination (infinite scroll)
      var path;
      if(this.source == "TIMELINE")
        path = "/api/posts/"
      else if(this.source == "USER_POSTS")
        path = "/api/users/" + this.$route.params.username + "/posts/"
      else if(this.source == "USER_LIKES")
        path = "/api/users/" + this.$route.params.username + "/likes/"
      else
        return

      fetch(path).then(function (response) {
          return response.json();
      }).then((result) => {
          this.posts = result.reverse();
      }).catch((err) => { 
          console.log(err); 
      });
    }
  }

}
</script>

<style>

</style>
