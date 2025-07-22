// 对axios二次封装
import axios from "axios";
 
// 1. 利用axios对象的方法create，去创建一个axios实例
// 2. request就是axios，只是稍微配置了一下
const requests = axios.create({
    // 基础路径，requests发出的请求在端口号后面会跟改baseURl
    baseURL:'/normal',
    timeout: 50000,//超时5秒，5秒没有响应就失败了
})
 
// 请求拦截器：在请求之前，请求拦截器可以检测到，可以在请求之前做一些事情
requests.interceptors.request.use((config)=>{
    // config:配置对象，对象里面有一个属性很重要，headers请求头
    return config;
})
 
// 响应拦截器
requests.interceptors.response.use((res)=>{
    debugger
    // 成功的回调函数:服务器响应数据回来以后，响应拦截器可以检测到，可以做一些事情
    return  res.data; 
},(error)=>{
    // 失败的回调函数
    console.log("响应失败"+error)
    return Promise.reject(new Error('fail'))
})
 
// 对外暴露
export default requests;
 