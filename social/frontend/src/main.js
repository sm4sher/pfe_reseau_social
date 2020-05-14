import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import App from './App.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(Vuex)

const routes = [
	// {
	// 	name: 'home',
	// 	path: '/',
	// 	component: Home,
	// },
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

const store = new Vuex.Store({
	state: {
		user: {
			id: 1,
			username: 'test',
			timeline: {
				posts: [
					{
						id: 1,
						author: null,
						text: "test post1",
					},
					{
						id: 2,
						author: null,
						text: "test post2",
					},
					{
						id: 3,
						author: null,
						text: "test post3",
					},
				],
			},
		},
	},
})

new Vue({
  render: h => h(App),
  store,
  router,
}).$mount('#app')
