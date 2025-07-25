from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.log_middleware import LogMiddleware



app = FastAPI(
    title='FastAPI Template',
    description='Just use in your project'
)

app.add_middleware(LogMiddleware)

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

@app.get('/ping',
        summary="Проверка работоспособности сервера",
        description='Этот эндпоинт выполняет простую проверку состояния сервера.',
        tags=['Health Check'],
        )
async def ping():
    return 'Server is running'