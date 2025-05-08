from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.logger.log_config import configure_logging

configure_logging()
logging.getLogger("watchfiles").setLevel(logging.WARNING)


app = FastAPI()


app = FastAPI(
    title='FastAPI Template',
    description='Just use in your project'
)

@app.get('/ping')
async def ping():
    return 'Server is running'


origins = [
    "http://localhost",  
    "http://localhost:8080",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)