"""
To build docker container run first build.sh, then run.sh
"""
from fastapi import FastAPI


app = FastAPI()


@app.get('/ping/', status_code=200)
async def get_ping():
    return {"message": "pong"}