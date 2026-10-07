import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Manage from '../views/Manage.vue'
import Company from '@/views/Company.vue'
import FrontPage from '../components/FrontPage'
import Mhome from '../components/Mhome.vue'
import CHome from '@/components/CHome.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    component: HomePage,
    children: [
      {
        path: '',
        redirect: 'front'
      },
      {
        path: 'front',
        component: FrontPage
      },
      {
        path: '/position',
        name: 'position',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/HomePosition.vue')
        }
      },
      {
        path: '/about',
        name: 'about',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/HomeResume.vue')
        }
      },
      {
        path: '/person',
        name: 'person',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/PersonPage.vue')
        }
      },
      {
        path: '/visual',
        name: 'visual',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/VisualPage.vue')
        }
      },
      {
        path: '/assess',
        name: 'assess',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/AssessPage.vue')
        }
      },
      {
        path: '/career-copilot',
        name: 'career-copilot',
        meta: { requiresAuth: true },
        component: () => import('../views/CareerCopilot.vue')
      },

    ]
  },
  {
    path: '/login',
    name: 'login',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/LoginPage.vue')
    }
  },
  {
    path: '/clogin',
    name: 'clogin',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/cLoginPage.vue')
    }
  },
  {
    path: '/register',
    name: 'register',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/RegisterPage.vue')
    }
  },
  {
    path: '/details',
    name: 'details',
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/DetailsPage.vue')
    }
  },
  // {
  //   path: '/mbti',
  //   name: 'mbti',
  //   component: function () {
  //     return import(/* webpackChunkName: "about" */ '../components/MbtiTest.vue')
  //   }
  // },
  // 公司
  {
    path: '/company',
    component: Company,
    children: [
      {
        path: '',
        redirect: 'CHome'
      },
      {
        path: 'CHome',
        component: CHome
      },
      {
        path: '/publish',
        name: 'publish',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/PublishPos.vue')
        }
      },
      {
        path: '/recommend',
        name: 'recommend',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/RecomResume.vue')
        }
      },
      {
        path: '/visualpos',
        name: 'visualpos',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/VisiualPos.vue')
        }
      },
    ]
  },
  // 管理员
  {
    path: '/manage',
    component: Manage,
    children: [
      {
        path: '',
        redirect: 'Mhome'
      },
      {
        path: 'Mhome',
        component: Mhome
      },
      {
        path: 'userma',
        name: 'userma',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/UserMana.vue')
        }
      },
      {
        path: 'posma',
        name: 'posma',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/PosMana.vue')
        }
      },
      {
        path: 'empma',
        name: 'empma',
        component: function () {
          return import(/* webpackChunkName: "about" */ '../views/EmpMana.vue')
        }
      },
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth) && !localStorage.getItem('token')) {
    next('/login')
  } else {
    next()
  }
})


export default router
