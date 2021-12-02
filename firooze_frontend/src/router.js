import { createRouter, createWebHistory } from "vue-router";
import home from './components/Home.vue'
import Notif from './components/Notif.vue'
import ContactUs from './components/Contact.vue'
import AboutUs from './components/About.vue'
import Charge from './components/Charge.vue'
import Admin from './components/Admin.vue'

const routes = [
    { path: '/', name: 'home', component: home },
    { path: '/notif', name: 'Notif', component: Notif },
    { path: '/ContactUs', name: 'contactus', component: ContactUs },
    { path: '/AboutUs', name: 'aboutus', component: AboutUs },
    { path: '/Charge', name: 'charge', component: Charge },
    { path: '/admin', name: 'Admin', component: Admin },
    // { path: '/aboutus', name: 'aboutus', component: aboutus },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
