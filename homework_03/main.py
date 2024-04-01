import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()


@app.get('/ping/', status_code=200)
async def get_ping():
    return {"message": "pong"}
#
#
# if __name__ == '__main__':
#     port = os.getenv('API_PORT', 8000)
#     uvicorn.run("main:app", host='0.0.0.0', port=port)