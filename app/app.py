from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() :
    return {"message" : "Hello world, 도커로 띄운 AI 서비스 준비 완료"}