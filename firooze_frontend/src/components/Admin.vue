<template>
  <div class="container py-5 mt-5 shadow px-3">

      <!-------------------- If User Loged In ----------------->
    <nav v-if="userLogin" class="navbar navbar-dark bg-light mb-2 rounded">
    <div class="container-fluid">
        <a class="nav-link text-shadow"><small class="text-secondary pe-2 text-shadow">خوش آمدید</small> {{ userNameNavbar }} </a>
        <form class="d-flex">
            <a class="nav-link text-danger text-shadow p-0" href="#" @click="logout" >خروج از حساب</a>
        </form>
    </div>
    </nav>

    <!------------------------------------------------------------>

    <button @click="goBack" class="btn btn-outline-dark btn-lg float-end display-block" >
        <i class="fa fa-arrow-left" aria-hidden="true"></i>
    </button>
    

      <!------------------- Check Password ---------------------->

    <div v-if="!userLogin">
        <div class="alert alert-danger"  style="width: 85%" role="alert">
           شما به پنل ادمین دسترسی ندارید. <a href="#" data-bs-toggle="collapse" data-bs-target="#passwordCollapse" class="alert-link">وارد شوید.</a>
        </div>

        <div class="collapse" id="passwordCollapse">
            <form class="row" @submit.prevent="login">
                <div class="col-sm-9 col-md-6 col-lg-4 col-xl-3"> <input v-model.trim.lazy="userName" class="form-control col-12 " placeholder="نام کاربری" type="text"> 
                <input v-model.trim.lazy="rmz" class="form-control mt-3 " placeholder="پسورد" type="password">
                <button class="btn btn-outline-dark mt-3"> ورود </button> </div>
            </form>
        </div>
    </div>
        <!--------------------- Charge ---------------------->
        <div v-if="userLogin">
        <p class="mt-5 mb-4 pt-5">
        <button class="btn btn-dark px-4" type="button" data-bs-toggle="collapse" data-bs-target="#chargeCollapse" >
            شارژ 
        </button>
        </p>
        <hr>
        <div class="collapse" id="chargeCollapse">
            <div class="p-0">
                <table class="table p-sm-0 table-striped table-hover mb-0">
                    <thead class="table-dark">
                        <tr class="h6 row">
                            <th class="col-sm-1" style="text-align: center; vertical-align: middle;" scope="col p-0">ردیف</th>
                            <th class="col-sm-4" style="text-align: center; vertical-align: middle;" scope="col">نام</th>
                            <th class="col-sm-3" style="text-align: center; vertical-align: middle;" scope="col">تلفن</th>
                            <th class="col-sm-2" style="text-align: center; vertical-align: middle;" scope="col">واحد</th>
                            <th class="col-sm-2" style="text-align: center; vertical-align: middle;" scope="col">بدهی</th>
                        </tr> 
                    </thead>
                    <tbody>
                        <tr class="tr row" v-for="(i, index) in resData" :key="index">
                            <td class="col-sm-1" style="text-align: center; vertical-align: middle;">{{i.id }}</td>
                            <td class="col-sm-4" style="text-align: center; vertical-align: middle;">{{i.name }}</td>
                            <td class="col-sm-3" style="text-align: center; vertical-align: middle;">{{ i.number }}</td>
                            <td class="col-sm-2" style="text-align: center; vertical-align: middle;">{{ i.unit }}</td>
                            <td class="col-sm-2 cursor mb-2 mb-sm-0" style="text-align: center; vertical-align: middle;" contenteditable="true" >{{ i.debt }}</td>
                        </tr>
                    </tbody>
                </table>
                <div class="row">
                    <button  @click="submit" class="btn d-block btn-lg btn-success col-sm-9 col-md-6 col-lg-5 col-xl-4 m-auto my-5" >ثبت</button>
                </div>
            </div>
        </div>
        </div>
        <!--------------------- Messages ---------------------->
        <div v-if="userLogin">
        <p class="mt-5 mb-4 pt-5">
        <button class="btn btn-dark px-4" type="button" data-bs-toggle="collapse" data-bs-target="#messageCollapse" >
            پیام ها 
        </button>
        </p>
        <hr>
        <div class="collapse m-auto" id="messageCollapse">
            <div class="p-0">
                <table class="table p-sm-0 table-striped table-hover mb-0">
                    <thead class="table-dark">
                        <tr class="h6 row">
                            <th scope="col" style="text-align: center; vertical-align: middle;" class="col-md-2" >نام</th>
                            <th scope="col" style="text-align: center; vertical-align: middle;" class="col-md-3" >ایمیل</th>
                            <th scope="col" style="text-align: center; vertical-align: middle;" class="col-md-6" >پیام</th>
                            <th scope="col" style="text-align: center; vertical-align: middle;" class="col-md-1" >زمان</th>
                        </tr> 
                    </thead>
                    <tbody class="">
                        <tr class="row" v-for="(m, index) in msgData" :key="index">
                            <td class="col-md-2" style="text-align: center; vertical-align: middle;" > <button @click="deleteMessage(m.id)" class="btn btn-danger py-0 px-2 float-start">X</button> {{m.name }} </td>
                            <td class="col-md-3" style="text-align: center; vertical-align: middle; word-break: break-all;" >{{m.email }}</td>
                            <td class="col-md-6 p-3" style="text-align: center; vertical-align: middle;">{{ m.msg }}</td>
                            <td class="col-md-1 time" style="text-align: center; vertical-align: middle; word-break: no-break;" >{{ m.time }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        </div>
        <!---------------------- Notifications ---------------------->
        <div v-if="userLogin">
        <p class="mt-5 mb-4 pt-5">
        <button class="btn btn-dark px-4" type="button" data-bs-toggle="collapse" data-bs-target="#notifCollapse" >
            اطلاعیه ها
        </button>
        <button class="btn btn-sm btn-success ms-3 px-4" type="button" data-bs-toggle="collapse" data-bs-target="#newNotifCollapse" >
            افزودن
        </button>
        </p>
        <hr>
        </div>
        <!---------------------- Notif Cards ---------------------->
 
        <div class="collapse" id="notifCollapse">
            <div class="row m-0 m-md-2" >
            <div class="col-sm-12 col-md-6 col-lg-4 mb-3" v-for="(post, index) in postData" :key="index">
                <div >
                    <div class="card ">
                        <div class="card-body">
                            <h4 class="card-title py-3 border-bottom" style="text-align: center; vertical-align: middle;" > {{ post.title }} </h4>
                            <p class="card-text px-2 pt-3 pb-4 border-bottom" style="text-align: justify " v-html="post.content" > </p>
                            <p class="card-text"><small class="text-muted"> {{ post.created_at }} </small>  <small class="float-end text-muted">{{ post.author }}</small></p>
                            <button @click="setEditPost(post.title, post.content, post.id)" type="button" class="btn btn-sm btn-outline-success float-start" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap" > تغییر این پست </button>
                            <button @click="deletePost(post.id)" class="btn btn-sm btn-outline-danger float-end"> حذف این پست </button>
                        </div>
                    </div>
                </div>
            </div>
            </div>
        </div>
        <!---------------------- New Notif ---------------------->

        <div class="collapse" id="newNotifCollapse">
            <div class="row m-0 m-md-2">
                <div class="col"></div>
                <div class="col-sm-12 col-md-9 col-lg-6 m-md-3 mb-3 shadow p-0 mb-md-0">
                    <div class="card ">

                        <div class="card-body mt-5 mb-2 mx-3">
                            <input v-model.trim.lazy="form.title" placeholder="عنوان" class="card-title form-control py-3 mb-4">
                            <textarea v-model.trim.lazy="form.content" rows="8" placeholder="بدنه" class="card-text form-control py-3 mb-4"></textarea>
                            <div class="row pt-5">
                                <button @click="submitNotif" class="col btn btn-sm py-2 btn-outline-success float-start"> افزودن </button>
                                <button @click="cancelNewPost" class="col btn btn-sm py-2 btn-outline-danger float-end"> لغو </button>
                            </div>
                        </div> 

                    </div>
                </div>
                <div class="col"></div>
            </div>
        </div>

        <!----------------------- Edit Post Modal ----------------------->

        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">تغییر پست</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                <div class="mb-3">
                    <label for="recipient-name" class="col-form-label">عنوان:</label>
                    <input type="text" class="form-control" v-model="editTitle" id="recipient-name">
                </div>
                <div class="mb-3">
                    <label for="message-text" class="col-form-label">بدنه:</label>
                    <textarea class="form-control" rows="6" v-model="editContent" id="message-text"></textarea>
                </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-danger" id="closeModal" data-bs-dismiss="modal"> لغو </button>
                <button @click="editPost" type="button" class="btn btn-success">‌ ثبت </button>
            </div>
            </div>
        </div>
        </div>

  </div>

</template>



<!------------------------------ SCRIPTS -------------------------------->
<script>
import axios from 'axios'
import { reactive, ref } from '@vue/reactivity'
import Swal from 'sweetalert2'
export default {
    setup(){
//-------------------- Varibles -------------------------

    var userName =ref('')

    var rmz =ref('')

    var userLogin=ref(false)

    var userNameNavbar = ref('')

    var editTitle = ref()

    var editContent = ref()

    var editPostId = ref()

    var debtList = []

    var resData = ref([])

    var msgData = ref([])

    var postData = ref([])

    var form = reactive({
        title : '',
        content : '',
        cover : '',
    })

//--------------------- Functions -------------------------

    function removeNavbar(){
            document.getElementById('navbar').remove()
        }
    removeNavbar()


    function removeBodyDark(){
        document.body.classList.remove('bg-dark')
    }
    removeBodyDark()


    function goBack(){
            location.replace("http://192.168.1.105:8080/")
        }


    function checkLocalStorage(){
        var localUserName = localStorage.getItem('userName')
        var localPassword = localStorage.getItem('rmz')
        if (localStorage.getItem('userName') !== null ){

        axios
        .post("http://127.0.0.1:8000/api-token-auth/", {
            username: localUserName,
            password: localPassword

        }).then(function(response){
            userNameNavbar.value = response.data.name
            userLogin.value = true
            userName.value = localUserName
            rmz.value = localPassword
            getData()

        }).catch(function(){
            userLogin.value = false
            localStorage.removeItem('userName')
            localStorage.removeItem('rmz')
        })
        }
    }
    checkLocalStorage()

    

    function login(){
        axios
        .post("http://127.0.0.1:8000/api-token-auth/", {
            username: userName.value,
            password: rmz.value

        }).then(function(){
            
            userLogin.value = true
            localStorage.setItem('userName' , userName.value)
            localStorage.setItem('rmz' , rmz.value)
            location.reload()

        }).catch(function(response){
            userName.value = ''
            rmz.value = ''
            console.log(response);
            Swal.fire('اطلاعات وارد شده صحیح نیست!', '', 'error')
        })
    }



    function logout(){
        localStorage.removeItem('userName')
        localStorage.removeItem('rmz')
        location.reload()
    }


    
    function submit(){
         Swal.fire({
             title: 'آیا از تغییر مبلغ بدهی اطمیمنان دارید؟',
             showDenyButton: true,
             confirmButtonText: 'بله',
             denyButtonText: `خیر`,
             }).then((result) => {

             if (result.isConfirmed) {
                 var trTags = document.getElementsByClassName('tr')
                    for(let i = 0; i < trTags.length; i++){
                        var residentId = trTags[i].firstChild.textContent
                        var residentDebt = trTags[i].lastChild.textContent
                        debtList.push({'id': residentId, 'debt': residentDebt})
                    }
                
                axios
                .post('http://127.0.0.1:8000/SubmitDebtAdmin/',{
                    username : userName.value,
                    password : rmz.value,
                    debtList : debtList
                }).then(function(){
                    Swal.fire('Saved!', '', 'success')
                }).catch(function(res){
                    console.log(res);
                    Swal.fire({
                        icon: 'error',
                        title: 'خطا در بروزرسانی اطلاعات!',
                        text: 'لطفا مقدار صحیح واردنمایید.',
                        })
                })
                
             }
             })
    }



    function getData(){
      axios
      .post('http://127.0.0.1:8000/GetResidentsAdmin/',{
        username : userName.value,
        password : rmz.value
      })
      .then(function(response){
        resData.value = response.data.data
      })
      .catch(function(response){
        var url = window.location
        var swalFooter = '<a href = "mailto:mahdi.haddadzadeh27@gmail.com?subject=Important Issue&body=In: ' + url + ' , ' + response + '">گزارش مشکل</a>'
        Swal.fire({
          icon: 'error',
          title: 'خطا در دریافت اطلاعات!',
          text: 'درحال حاضر امکان دریافت اطلاعات ساکنین از سرور وجود ندارد',
          footer: swalFooter
        })
      })


      axios
      .post('http://127.0.0.1:8000/GetMessageAdmin/',{
        username : userName.value,
        password : rmz.value
      })
      .then(function(response){
        msgData.value = response.data.data
        msgData.value.forEach(() => {
        });
      })
      .catch(function(response){
        var url = window.location
        var swalFooter = '<a href = "mailto:mahdi.haddadzadeh27@gmail.com?subject=Important Issue&body=In: ' + url + ' , ' + response + '">گزارش مشکل</a>'
        Swal.fire({
          icon: 'error',
          title: 'خطا در دریافت اطلاعات!',
          text: 'درحال حاضر امکان دریافت پیام های ارسال شده وجود ندارد.',
          footer: swalFooter
        })
      })
      axios
      .post('http://127.0.0.1:8000/GetPosts/',{
        userName : userName.value,
        password : rmz.value
      })
      .then(function(response){
        postData.value = response.data.postData

      })
      .catch(function(response){
        var url = window.location
        var swalFooter = '<a href = "mailto:mahdi.haddadzadeh27@gmail.com?subject=Important Issue&body=In: ' + url + ' , ' + response + '">گزارش مشکل</a>'
        Swal.fire({
          icon: 'error',
          title: 'خطا در دریافت اطلاعات!',
          text: 'درحال حاضر امکان دریافت اطلاعیه ها از سرور وجود ندارد.',
          footer: swalFooter
        })
      })
    }



    function deleteMessage(id){
        axios
        .post('http://127.0.0.1:8000/DeleteMessage/', {
            username : userName.value,
            password : rmz.value,
            id : id
        })
        .then(function () {
            getData()
            
        }).catch(function(){
            Swal.fire('خطا در حذف پست!', '', 'error')
        })
    }

    


    function submitNotif(){
        if (userLogin.value==false){    
            login()
        }
        axios
        .post('http://127.0.0.1:8000/SubmitNotif/', {
        title : form.title,
        content : form.content,
        username : userName.value,
        password : rmz.value,
      })
      .then(function(){
        Swal.fire('افزودن پست با موفقیت انجام شد!', '', 'success')
        form.title = ''
        form.content = ''
        getData()

        }).catch(function(){
            alert('خطا در افزودن اطلاعیه لطفا تمام فیلدها را به درستی پر کنید.')
          
        })
    }


    function cancelNewPost() {
        form.title = '',
        form.content = ''
    }


    function setEditPost(title, content, id){
        // modal is opening now
        editTitle.value = title
        editContent.value = content
        editPostId.value = id
    }


    function editPost() {
        axios
        .post('http://127.0.0.1:8000/EditPost/', {
            username: userName.value,
            password: rmz.value,
            id: editPostId.value,
            title: editTitle.value,
            content: editContent.value,
        })
        .then(function(){
            Swal.fire('تغییرات اعمال شد', '', 'success')
            editTitle.value = ''
            editContent.value = ''
            editPostId.value = ''
            document.getElementById('closeModal').click()
            getData()
        })
        .catch(function(){
            Swal.fire('خطا در تغییر پست!', '', 'error')
        })
    }



    function deletePost(postId) {
        axios
        .post('http://127.0.0.1:8000/DeletePost/',{
            username : userName.value,
            password : rmz.value,
            id : postId,
        })
        .then(function(res){
            console.log(res)
            Swal.fire('پست حذف شد', '', 'success')
            getData()
        })
        .catch(function(){
            Swal.fire('خطا در حذف پست!', '', 'error')
        })
    }  


    return {resData, msgData,postData,userName, rmz, userLogin, goBack,
    submit, submitNotif, form, cancelNewPost, deletePost, setEditPost,
    editPost, editTitle, editContent, login, userNameNavbar, logout,
    deleteMessage}
  }
}
</script>

<style>

.cursor{
    cursor: text !important;
    border: 1px solid gray;
    text-align: center;
    background-color: rgba(255, 235, 205, .4) !important;
}
.cursor:focus{
    background-color: white !important;
}
.w-60{
    width: 60%;
}
.text-shadow{
    text-shadow: 1px 1px 1px black;
}
</style>