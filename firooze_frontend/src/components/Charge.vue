<template >

  <div class="position-relative pb-5 pt-10 container-lg bg-dark shadow px-0 px-sm-2 px-md-3">
    
<div class="row">
  <div class="col"></div>
    <div class="mt-5 col-10 col-sm-9 col-md-6" style="text-align: center">
      <center class="text-light h5 mb-5 border-bottom pb-3 border-warning"> برای مشاهده بدهی اطلاعات واحد خود را از فیلدهای زیر انتخاب کنید. </center>
      <select v-model="block" class="form-select btn-warning" aria-label="Default select example">
        <option selected> بلوک</option>
        <option value="ف ۱">فیروزه ۱</option>
        <option value="ف ۲">فیروزه ۲</option>
        <option value="ز ۱">زمرد ۱</option>
        <option value="ز ۲">زمرد ۲</option>
      </select>

      <select v-model="floor" class="form-select  btn-warning my-5" aria-label="Default select example">
        <option selected>طبقه</option>
        <option value="1">اول</option>
        <option value="2">دوم</option>
        <option value="3">سوم</option>
        <option value="4">چهارم</option>
        <option value="5">پنجم</option>
        <option value="6">ششم</option>
        <option value="7">هفتم</option>
        <option value="8">هشتم</option>
      </select>

      <select v-model="unit" class="form-select my-5 btn-warning" aria-label="Default select example">
        <option selected>واحد</option>
        <option value="1">یک</option>
        <option value="2">دو</option>
        <option value="3">سه</option>
        <option value="4">چهار</option>
      </select>

      <button :disabled='disable' @click="show" class="btn btn-outline-warning w-100 py-2" style="box-shadow: 4px 4px 5px rgba(240, 255, 0, .3) !important"> <i v-if="loading" class="fas fa-circle-notch fa-spin"></i>  مشاهده بدهی  </button> 
    </div>
    <div class="col"></div>
    <p>
      <button class="d-none" id="collapse" type="button" data-bs-toggle="collapse" data-bs-target="#showDebt"> </button>
    </p>

    <div class="collapse" id="showDebt">
      <div class="card bg-secondary text-light card-body py-4" style="text-shadow: 2px 2px 2px black">
          <div style="text-align: center">
            آقا/خانم <div class="text-decoration-underline px-2" style="display: inline;">{{name}}</div> بدهی شما {{debt}} تومان میباشد.
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
    const block= ref('بلوک')
    const floor= ref('طبقه')
    const unit= ref('واحد')
    const debt= ref()
    const name= ref()
    const disable = ref(false)
    var data = ref([]);

    var loading = ref(false)

    function bodyDark(){
      document.body.classList.add('bg-dark')
    }
    bodyDark()

    function reloadPage(){
      window.location.reload()
    }

    function show(){
      if (block.value == 'بلوک' || floor.value == 'طبقه' || unit.value == 'واحد') {
        Swal.fire('لطفا موارد خواسته شده را انتخاب کنید!', '', 'error')
      } else{
      loading.value = true
      disable.value = true
      axios
      .post('http://127.0.0.1:8000/GetDebt/',{
        block : block.value,
        floor : parseInt(floor.value),
        unit : parseInt(unit.value),
      })
      .then(function(res){
        loading.value = false
        debt.value = res.data.data.debt
        name.value = res.data.data.name

        document.getElementById('collapse').click()

      })
      .catch(function(res){
        loading.value = false
        disable.value = false
        if (res.response.status == 404) {
          Swal.fire('ساکنی با مشخصات وارد شده یافت نشد!', '', 'error')
        } else {
          Swal.fire('امکان دریافت اطلاعات از سرور وحود ندارد!', '', 'error')
        }
        
      })
      }

    }

    return {data, loading, block, floor, unit, show, debt, name, disable, reloadPage}
  }
}
</script>

<style>

.bg-orangered{
  background-color: orange;
}
.height-100{
  height: 60vw;
}

</style>