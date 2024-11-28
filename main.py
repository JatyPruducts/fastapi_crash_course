from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("SystemText: DataBase was cleared")
    await create_tables()
    print("SystemText: DataBase is ready for work")
    yield
    print("SystemText: DataBase was closed")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

