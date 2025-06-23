
from fastapi import FastAPI
import os,logging

from core import Router


PATH = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(
    description='''HTTP状态码描述:

    200 OK: 请求成功。
    201 Created: 创建了新的资源。
    204 No Content: 请求成功，但没有实体内容。
    400 Bad Request: 请求格式错误。
    401 Unauthorized: 未授权。
    403 Forbidden: 禁止访问。
    404 Not Found: 未找到资源。
    500 Internal Server Error: 服务器内部错误。'''
)

app.include_router(Router.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}


port = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    import uvicorn

    logging.root.setLevel(logging.INFO)

    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)