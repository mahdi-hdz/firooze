<template>

<div class="color-bg shape container">
  <div class="position-relative  pb-5 pt-10 row justify-content-center">

    <div class="h2 text-light pb-3 col-sm-9 px-lg-0 col-lg-8">فرم ارسال پیام</div>
    <br>
    <div class="pt-5 px-lg-4 col-sm-9 col-lg-4 ">
      <input v-model="form.name" type="text" class="form-control form-control-lg"  placeholder="نام کامل">
    </div>
    <br>
    <div class="pt-3 px-lg-1 col-sm-9 col-lg-4 ">
      <label for="exampleFormControlInput1" class="form-label">ایمیل</label>
      <input v-model="form.email" type="email" class="form-control form-control-lg" id="exampleFormControlInput1" placeholder="name@example.com">
    </div>
    <br>
    <div class="pt-5 col-sm-9 px-sm-0 col-lg-8 ">
      <textarea @keyup="remain" @keydown="remain" maxlength="400" v-model="form.message" class="form-control form-control-lg" placeholder="پیام" rows="4"></textarea>
      <small class="ps-2"> {{remainChar}} کاراکتر باقی مانده </small>
    </div>

    <div class="pt-5 col-sm-9 px-sm-0 col-lg-8">
      <button v-on:click="send" class="btn btn-lg btn-secondary btn-bg w-100 py-2" :disabled=disable > {{sumbit}} <small v-if="disable">{{countDown}}</small> <i v-if="loading" class="fas fa-circle-notch fa-spin"></i> </button>
    </div>
  </div>
</div>

 
</template>

<script>
import axios from 'axios'
import { reactive, ref } from '@vue/reactivity'
import swal from "sweetalert";
import Swal from 'sweetalert2';

export default {
  setup(){
    const sumbit=ref('ارسال')
    const countDown = ref()
    const disable=ref(false)
    const loading=ref(false)
    let remainChar = ref(400)
    const form=reactive({
      name:'',
      email:'',
      message:''
    })

    function remain(){
      remainChar.value = 400 - form.message.length
    }

    function send(){
      if (form.name == ''){
        countDown.value = ''
        sumbit.value = 'فیلدهارا بررسی نمایید!'
        disable.value = true
        setTimeout(()=>{ sumbit.value='ارسال'; disable.value=false}, 
        3000)
      }else{
        disable.value= true
        loading.value= true
        axios
        .post('http://127.0.0.1:8000/SendMessage/', {
          senderName : form.name,
          senderEmail : form.email,
          message : form.message ,
        }).then(function(){
          swal({
                title: "",
                text: "پیام با موفقیت ارسال شد !",
                icon: "success",
                button: "OK",
              }),
            loading.value= false
            form.name = ''
            form.message = ''
            form.email = ''
            sumbit.value = 'ارسال مجدد پیام در '
            countDown.value = 30
            setTimeout(() => {
              disable.value=false
            }, 30000);
            
            function a(){
              if (countDown.value > 0) {
              setTimeout(() => {
                countDown.value -= 1
                a()
              }, 1000)
            }else{
              sumbit.value = 'ارسال'
            }
            }
            a()
            


        }).catch(function(response){
          loading.value= false
          if (response == 'Error: Network Error'){
            var url = window.location
            var swalFooter = '<a href = "mailto:mahdi.haddadzadeh27@gmail.com?subject=Important Issue&body=In: ' + url + ' , ' + response + '">گزارش مشکل</a>'
            disable.value = false
            Swal.fire({
              icon: 'error',
              title: 'خطا سرور!',
              text: 'درحال حاضر امکان ارسال پیام وجود ندارد‌‌‌.',
              footer: swalFooter
            })
          }
          else{
            Swal.fire('خطا در ارسال پیام لطفا تمام فیلدها را به درستی پر کنید.', '', 'error')
            disable.value = false
          }
        })
      }

      
    }

    return {send, sumbit, form, disable, countDown, loading, remainChar, remain}
  }
}
</script>

<style>
.pt-10{
  padding-top: 130px;
}

.shape{
background-image: url(../assets/wave.webp);
height: 100vh;
min-width: 200px;
background-size: cover;
background-repeat: no-repeat;
max-width: 100%;
background-position: center center !important;
overflow: hidden;
position: relative;
}

.color-bg{
  background-color: rgb(255, 150, 0)
}

.h2{
  text-shadow: 3px 3px 5px black;
}
</style>