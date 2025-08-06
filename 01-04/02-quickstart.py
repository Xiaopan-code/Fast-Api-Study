from fastapi import FastAPI
import uvicorn
#没加async默认同步 加了就是异步  FastAPI 异步多

app = FastAPI()

@app.get("/")
async def home():
    return {"user_id": 1001}

@app.get("/shop")
async def home():
    return {"shop": "商品信息"}

if __name__ == "__main__":
    uvicorn.run("02-quickstart:app", port=8000, reload=True)