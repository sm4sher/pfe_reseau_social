import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import App from './App.vue'

//import Home from './components/Home.vue'
import Profile from './components/Profile.vue'

import PostList from './components/PostList.vue'
import UserList from './components/UserList.vue'

import Landing from './components/Landing.vue'
import Login from './components/Login.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(Vuex)

const routes = [
	{
		path: '/',
		component: Landing
		//redirect: '/home'
	},
	{
		name: 'home',
		path: '/home',
		component: PostList,
		props: {source: "TIMELINE", title: "Home", newpostPrompt: true},
		meta: {requiresAuth: true},
	},
	{
		path: '/user/:username',
		component: Profile,
		meta: {requiresAuth: true},
		children: [
			{
				name: 'profile',
				path: '',
				component: PostList,
				props: {source: "USER_POSTS", title: "", newpostPrompt: false}
			},
			{
				name: 'profile-likes',
				path: 'likes',
				component: PostList,
				props: {source: "USER_LIKES", title: "", newpostPrompt: false}
			},
			{
				name: 'profile-followers',
				path: 'followers',
				component: UserList,
				props: {source: "USER_FOLLOWERS"}
			},
			{
				name: 'profile-following',
				path: 'following',
				component: UserList,
				props: {source: "USER_FOLLOWING"}
			},
		],
	},
	{
		name: 'login',
		path: '/login',
		component: Login,
	},
	// {
	// 	name: 'register',
	// 	path: '/register',
	// 	component: Register,
	// },
	// {
	// 	name: 'post',
	// 	path: '/post/:post_id',
	// 	component: Post,
	// }
]

const router = new VueRouter({
	routes,
})


Vue.filter('formatDateTime', function(value) {
  if (value) {
    return new Date(parseInt(value)).toLocaleString(); //Value peut être String ou int
  }
})

const store = new Vuex.Store({
	state: {
		user: null,
		// user: {
		// 	id: 1,
		// 	username: 'user1',
		// 	profile: {
		// 		display_name: 'User 1',
		// 		picture: "profile_default.jpeg",
		// 	}
		// },
	},
	getters: {
		islogged: state => {
			return state.user != null;
		}
	},
	mutations: {
		login(state, user){
			state.user = user;
			Vue.set(state, "user", user)
		},
		logout(state){
			state.user = null;
			Vue.set(state, "user", null)
		},
	}
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (store.state.user === null) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next() // make sure to always call next()!
  }
})

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

Vue.mixin({
	methods: {
		getToken(){
			return readCookie('csrftoken');
		}
	}
})

new Vue({
  render: h => h(App),
  store,
  router,
}).$mount('#app')
