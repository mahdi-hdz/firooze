<template>
  <div >
    <!-- navbar sestion -->
    <section id="navbar" >
      <nav class="navbar navbar-expand-md navbar-blur-bg navbar-dark position-absolute w-100" style="z-index: 100; ">
        <div class="container-sm">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <router-link class="nav-link active" to="/">صفحه اصلی</router-link>
              </li>
              <li class="nav-item ps-3">
                <router-link class="nav-link active" to="/AboutUs">معرفی مجتمع</router-link>
              </li>
              <li class="nav-item ps-3">
                <router-link class="nav-link active" to="/Charge">مشاهده و پرداخت شارژ</router-link>
              </li>
              <li class="nav-item ps-3">
                <router-link class="nav-link active" to="ContactUs" >تماس با هیأت مدیره</router-link>
              </li>
              <li class="nav-item ps-3">
                <router-link class="nav-link active" to="/Notif">اصلاعیه ها</router-link>
              </li>
            </ul>
          </div>
          
        </div>
      </nav>
    </section>

    <router-view></router-view>


  </div>
</template>


<script>



export default {
  name: "App",
  setup(){
    
  }
};
</script>

<style>
@import url("./assets/bootstrap.css");



@media screen and (max-width: 767px) {
  .navbar-blur-bg{
    background: rgb(50, 50, 50) !important;
  }

  .time{
    border-bottom: 2px dashed gray !important;
  }


}
.nav-link:after {
  content: '';
  display: block;
  margin: 5px auto 0px auto;
  height: 2px;
  width: 0px;
  background: transparent;
  transition: width .5s ease, background-color .5s ease;
}

.router-link-active:after {
  width: 100%;
  background: #fff;
}

.home-bg{
background-image: url('./assets/home-image.jpg');
height: 100vh;
min-width: 200px;
background-size: cover;
background-repeat: no-repeat;
max-width: 100%;
background-position: center center !important;
overflow: hidden;
position: relative;
}

.navbar-blur-bg{
  background: rgba(50,50,50,.6);
}

.nav-item{
  text-shadow: 1px 1px 1px black;
}
</style>
