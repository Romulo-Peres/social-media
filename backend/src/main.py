from dotenv import load_dotenv
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database.connection import create_database_pool
from controllers.post_controller import post_router
from controllers.user_controller import user_router
import time
import os

load_dotenv()

while True:
    try:
        create_database_pool()
        print('Database is up! Let\'s go!')
        break
    except Exception as e:
        print('The system database isn’t up yet. Retrying in 5 seconds...')
        time.sleep(5)

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": f"Validation failed: {exc.errors()[0]['msg']}"}
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router)
app.include_router(user_router)
