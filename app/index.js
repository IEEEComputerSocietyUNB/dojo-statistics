import Vue from 'vue/dist/vue.common'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import VueMdl from 'vue-mdl'

import App from './App.vue'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(VueMdl)

let router = new VueRouter()

router.map({
    '/home': { component: Home },
    '/login': { component: Login }
})

router.redirect({
    '*': '/home'
})

router.start(App, '#app')
