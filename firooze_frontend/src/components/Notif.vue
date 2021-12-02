<template>

  <div class="container position-relative bg-warning pt-10"> 

            <div class="row m-0 m-md-2" >
                <div class="col-sm-12 col-md-6 col-lg-4 my-4" v-for="(post, index) in posts" :key="index">
                    <div class="card h-100">
                        <div class="card-body">
                            <h4 class="card-title py-3 border-bottom" style="text-align: center; vertical-align: middle;" > {{ post.title }} </h4>
                            <p class="card-text px-2 pt-3 pb-4 border-bottom" style="text-align: justify " v-html="post.content" > </p>
                            <p class="card-text"><small class="text-muted"> {{ post.created_at }} </small> <small class="text-muted float-end">{{ post.author }}</small> </p>
                          
                        </div>
                    </div>
                </div>

            </div>
        </div>

</template>

<script>
import axios from 'axios'
import { ref } from '@vue/reactivity'
import Swal from 'sweetalert2'
export default {
  setup(){
    
function removeBodyDark(){
  document.body.classList.remove('bg-dark')
    }
    removeBodyDark()
    var posts = ref([])
    axios
    .post('http://127.0.0.1:8000/GetPosts/')
    .then(function(response){
      posts.value = response.data.postData

    }).catch(function(response){
      var url = window.location
        var swalFooter = '<a href = "mailto:mahdi.haddadzadeh27@gmail.com?subject=Important Issue&body=In: ' + url + ' , ' + response + '">گزارش مشکل</a>'
        Swal.fire({
          icon: 'error',
          title: 'خطا در دریافت اطلاعات!',
          text: 'درحال حاضر امکان دریافت اطلاعیه ها از سرور وجود ندارد',
          footer: swalFooter
        })


    })
  return{posts, }
  }
}
</script>

<style>

</style>