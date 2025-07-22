import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],

 server: {
    proxy: {
      '/v1': {
        target: 'http://127.0.0.1:8000/', // 后端地址
        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/api/, '') // 根据实际情况调整
      }
    }
  }
})
