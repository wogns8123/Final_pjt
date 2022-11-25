import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/movie/MovieView.vue'
import HomeView from '@/views/movie/HomeView'
import LogInView from '@/views/account/LogInView'
import SignupView from '@/views/account/SignupView'
import ProfileView from '@/views/account/ProfileView'
import MovieSearch from '@/views/movie/MovieSearch'
// import CommunityView from '@/views/community/CommunityView'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/movies/search',
    name: 'search',
    component: MovieSearch,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
