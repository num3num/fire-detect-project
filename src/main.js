import { createApp } from 'vue'
import App from './App.vue'
import '../src/assets/styles/main.css';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './router/router'; // 引入路由配置文件

const app = createApp(App)
app.use(ElementPlus)
app.use(router); // 使用路由实例
app.mount('#app')
