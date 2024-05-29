from fastapi import FastAPI
from todo import todo_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["http://127.0.0.1:5500", "35.169.119.254"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @는 decorator. 주소 뒤에 "/"가 붙음.
# 만약 @app.get("/ddd")라면 0.0.0.0:8000/ddd가 됨.
# 0.0.0.0:8000/ 로 들어오면 아래를 실행하겠다는 의미
@app.get("/") 
async def welcome() -> dict:
    return {
        "msg" : "Hello world!"
    }

app.include_router(todo_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True) 