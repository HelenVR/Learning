import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/ping/', status_code=200)
async def get_ping():
    return {"message": "pong"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000)