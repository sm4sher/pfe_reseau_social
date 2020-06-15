<template>
  <div class="login box">
    <h2 class="title is-2">Login</h2>
    <form>
      <div class="field">
        <label class="label">Username</label>
        <div class="control has-icons-left">
          <input v-model="username" class="input is-success" type="text" placeholder="Username">
          <span class="icon is-small is-left">
            <i class="fas fa-user"></i>
          </span>
        </div>
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control has-icons-left">
          <input v-model="password" class="input is-success" type="password">
          <span class="icon is-small is-left">
            <i class="fas fa-key"></i>
          </span>
        </div>
        <p class="help is-success">This username is available</p>
      </div>

      <div class="field is-grouped is-horizontal">
        <div class="control">
          <button v-on:click="doLogin" class="button is-link">Login</button>
        </div>
        <label class="field-label is-normal">Don't have an account?</label>
        <div class="control">
           <button class="button">Register</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>

export default {
  name: 'Login',
  components: {

  },
  data(){
    return {
      username: "",
      password: "",
    }
  },
  mounted(){

  },
  methods: {
    doLogin(){
      if(this.username === "" || this.password === "")
        return;
      
      // var ta = document.getElementById("newpost-content");
      // var tac = document.getElementById("newpost-content-control");
      // tac.classList.add("is-loading");
      var data = {
        username: this.username,
        password: this.password,
      }
      fetch("/api/login/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      }).then((response) => {
        console.log(response);
        return response.json()
        // tac.classList.remove("is-loading");
        // if(response.status === 201){
        //   ta.classList.add("is-success");
        //   this.text = "";
        //   return response.json();
        // }
        // else {
        //   ta.classList.add("is-danger");
        //   throw Error;
        // }
      }).then((result) => {
        console.log("result:")
        console.log(result);
        if(result.status === "success"){
          this.$store.commit('login', result.user)
          this.$router.push('home')
        }
        else {
          //
        }
      }).catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.login {
  width: 50%;
  margin: auto;
  margin-top: 4rem; 
  /*background-color: #EEEEEE;*/
}
</style>
