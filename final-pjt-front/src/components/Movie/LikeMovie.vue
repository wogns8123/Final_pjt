<template>
  <div>
    <button class="buttonSize" style="color:#ea4335" @click="likeMovie">
      <img v-if="this.likestatus === false" src="@/assets/images/like_.png" style="width:100px">
      <img v-else src="@/assets/images/like_check.png" style="width:100px">
    </button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "LikeMovie",
  data(){
    return {
      likestatus: false,
    }
  },
  props: {
    movie: Object
  },
  methods: {
    likeMovie() {
      const commentItemSet = {
        content: this.content,
          movie: this.movie
        }
      axios({
        
        method: "post",
        url: `${API_URL}/api/v1/movies/${this.movie.id}/like_users/`,
        data: {
          movie: commentItemSet.movie,
        },
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          if (this.likestatus === false){
            this.likestatus = true
          }else{
            this.likestatus = false
          }
        })
        .catch((err) => {
          console.log(err);
        })
      },
      getStatus(){
        axios({
          method: 'post',
          url:`${API_URL}/accounts/movies/`,
          headers:{
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(res=>{
          if (res.data.like_movies.includes(this.movie.id)) {
            this.likestatus = true
          } else{
            this.likestatus = false
          }
        })
        .catch(err=>{
          console.log(err)
        })
      }
    },
    created(){
      this.getStatus()
    }
}
</script>

<style>
.buttonSize{
  width: 100px;
}
</style>
