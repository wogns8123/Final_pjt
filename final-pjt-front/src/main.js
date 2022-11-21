import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


import Vuetify from 'vuetify'

Vue.use(Vuetify)

Vue.use(BootstrapVue)

Vue.use(VueGlide)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
