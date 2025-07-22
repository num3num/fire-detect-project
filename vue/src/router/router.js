// router/index.js 或 router/index.ts
import {
  createRouter,
  createWebHistory
} from 'vue-router';
import Login from '../components/login/HelloWorld.vue';
// import Document from '../components/document/index.vue';
import TopNavbar from '../components/TopNavbar/TopNavbar.vue';
const routes = [{
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/topNavbar',
    name: 'TopNavbar',
    component: TopNavbar,
  },
  // {
  //   path: '/document',
  //   name: 'Document',
  //   component: Document,
  // },
];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(
    import.meta.env.BASE_URL), // 使用HTML5 history模式
  routes // 注入路由配置
})

export default router;