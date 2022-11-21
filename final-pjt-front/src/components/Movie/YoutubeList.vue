<template>
<<<<<<< HEAD
  <ul class="youtube-list">
=======
  <div>
>>>>>>> f3a832f2061c1aa9a514e86b812620dd0aebba9f
    <YoutubeListItem class="container"
    v-for="(video) in this.youtubeVideo"
    :key="video.idx"
    :video="video"
<<<<<<< HEAD
    />    
  </ul>
=======
    
    />
    
  </div>
>>>>>>> f3a832f2061c1aa9a514e86b812620dd0aebba9f
</template>

<script>
import YoutubeListItem from '@/components/Movie/YoutubeListItem'

<<<<<<< HEAD

=======
>>>>>>> f3a832f2061c1aa9a514e86b812620dd0aebba9f
export default {
  name: 'YoutubeList',
  props: {
    movie: Object,
  },
  components:{
    YoutubeListItem
  },
  data(){
    return{
      youtubeVideo: this.$store.state.youtubeVideos
<<<<<<< HEAD
=======
      
>>>>>>> f3a832f2061c1aa9a514e86b812620dd0aebba9f
    }
  },
  created(){
    this.$store.dispatch('getYoutube', this.movie.title)
  }
}
</script>

<style>
<<<<<<< HEAD
.youtube-list{
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-around;
  list-style-type: none;
  padding-left: 0;
}

=======
>>>>>>> f3a832f2061c1aa9a514e86b812620dd0aebba9f

</style>