import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

// styles

import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/styles/tailwind.css";


// layouts

import Admin from "@/layouts/Admin.vue";
import Auth from "@/layouts/Auth.vue";

// views for Admin layout

import Dashboard from "@/views/admin/Dashboard.vue";
import MyAccount from "@/views/admin/MyAccount.vue";
import Search from "@/views/admin/Search.vue";

// views for Auth layout

import Login from "@/views/auth/Login.vue";
import Register from "@/views/auth/Register.vue";
import Activation from '@/views/auth/Activation.vue';
import PasswordReset from '@/views/auth/PasswordReset.vue'
import PasswordResetConfirm from '@/views/auth/PasswordResetConfirm.vue'
import ResendActivation from '@/views/auth/ResendActivation.vue'


// views without layouts

import Landing from "@/views/Landing.vue";


const routes = [
  {
    path: "/admin",
    redirect: "/admin/dashboard",
    component: Admin,
    children: [
      {
        path: "/admin/dashboard",
        name: "Dashboard",
        component: Dashboard,
        meta: {
          requiredLogin: true
        }
      },
      {
        path: "/admin/my-account",
        name: 'MyAccount',
        component: MyAccount,
        meta: {
          requiredLogin: true
        }
      },
      {
        path: "/admin/search",
        name: 'Search',
        component: Search,
        meta: {
          requiredLogin: true
        }
      },
    ],
  },
  {
    path: "/auth",
    redirect: "/auth/login",
    component: Auth,
    children: [
      {
        path: "/auth/login",
        name: "Login",
        component: Login,
      },
      {
        path: "/auth/register",
        name: "Register",
        component: Register,
      },
      {
            path: '/accounts/users/activation/:uid?/:token?',
            name: 'Activation',
            component: Activation,
          },
      {
        path: '/auth/password_reset',
        name: 'PasswordReset',
        component: PasswordReset,
      },
      {
            path: '/accounts/users/reset_password_confirm/:uid?/:token?',
            name: 'PasswordResetConfirm',
            component: PasswordResetConfirm,
      },
      {
            path: '/auth/resend_activation',
            name: 'ResendActivation',
            component: ResendActivation,
      },
    ],
  },
  {
    path: "/",
    name: "Landing",
    component: Landing,
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiredLogin) && !store.state.isAuthenticated) {
    next("/auth/login")
  } else {
    next()
  }
})
export default router
