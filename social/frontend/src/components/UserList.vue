<template>
  <div>
    <div v-for="user in users" :key="user.id">
      {{ user.username }}
    </div>
  </div>
</template>

<script>

export default {
  name: 'UserList',
  components: {

  },
  props: {
    source: String,
  },
  data(){
    return {
      users: Array,
    }
  },
  mounted(){
    this.loadPosts();
  },
  methods: {
    addPost(post){
      this.posts.unshift(post);
    },
    loadUsers(){
      var path;
      if(this.source == "USER_FOLLOWERS")
        path = "/api/users/" + this.$route.params.username + "/followers"
      else if(this.source == "USER_FOLLOWING")
        path = "/api/users/" + this.$route.params.username + "/following"
      else
        return

      fetch(path).then(function (response) {
          return response.json();
      }).then((result) => {
          this.users = result;
      }).catch((err) => { 
          console.log(err); 
      });
    }
  }

}
</script>

<style>

</style>
