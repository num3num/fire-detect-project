```
此项目使用了vue3+elementPlus
```

安装环境:
```
1.安装node -18.9.0
```
项目启动:
```
1.打开当前项目路径cmd
2.npm i
3.npm run dev
```
如需打包:
```
npm run build
```
测试方式
```
curl -X 'POST' \
  'http://127.0.0.1:8000/v1/detect?file_path={file_path}&sava_path={sava_path}' \
  -H 'accept: application/json' \
  -d ''
```
