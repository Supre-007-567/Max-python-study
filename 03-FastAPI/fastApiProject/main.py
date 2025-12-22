
from fastapi import FastAPI
import uvicorn
# 创建 fastapi实例
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World66"}


@app.get("/hello")
async def get_hello():
    return {"msg": "hello fastAPi"}


@app.get("/user/hello")
async def get_user_hello():
    return {"msg": "我正在学习fastApi"}
