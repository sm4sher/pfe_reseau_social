import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import App from './App.vue'

import Home from './components/Home.vue'
//Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(Vuex)

const routes = [
	{
		name: 'home',
		path: '/',
		component: Home,
	},
	// {
	// 	name: 'login',
	// 	path: '/login',
	// 	component: Login,
	// },
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
    return new Date(parseInt(value)).toLocaleTimeString(); //Value peut être String ou int
  }
})

const store = new Vuex.Store({
	state: {
		user: {
			id: 1,
			username: 'test',
			profile: {
				picture: "/static/social/img/profile_default.jpeg",
			}
		},
	},
})

new Vue({
  render: h => h(App),
  store,
  router,
}).$mount('#app')
