import { createApp } from 'vue'
import App from '../src/App.vue'
import router from './router.js'
import CKEditor from '@ckeditor/ckeditor5-vue';

const app = createApp(App).use(router)
app.use(router, CKEditor)
app.mount('#app')