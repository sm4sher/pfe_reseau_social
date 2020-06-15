<template>
  <article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img class="is-rounded" :src="'/static/social/img/'+$store.state.user.profile.picture">
    </p>
  </figure>
  <div class="media-content">
    <div class="field">
      <p class="control is-medium" id="newpost-content-control">
        <textarea v-model="text" rows="3" id="newpost-content" class="textarea has-fixed-size" placeholder="Add a post..."></textarea>
      </p>
    </div>
    <nav class="level">
      <div class="level-left">
        <div class="level-item">
          <a class="button is-info" v-on:click="newPost">Submit</a>
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
  data(){
    return {
      text: ''
    }
  },
  created(){
    
  },
  methods: {
    newPost: function(){
      if(this.text == "")
        return;
      
      var ta = document.getElementById("newpost-content");
      var tac = document.getElementById("newpost-content-control");
      tac.classList.add("is-loading");
      var data = {
        text: this.text
      }
      fetch("/api/posts/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.getToken()
        },
        body: JSON.stringify(data)
      }).then((response) => {
        console.log(response);
        tac.classList.remove("is-loading");
        if(response.status === 201){
          ta.classList.add("is-success");
          this.text = "";
          return response.json();
        }
        else {
          ta.classList.add("is-danger");
          throw Error;
        }
      }).then((result) => {
        console.log("result:")
        console.log(result);
        this.$emit('new-post', result);
      }).catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style>

</style>
