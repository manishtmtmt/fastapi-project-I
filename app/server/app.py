from fastapi import FastAPI

from app.server.routes.student import router as student_router


app = FastAPI()


app.include_router(student_router, tags=["Student"], prefix="/api/students")


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to this fantastic main_app!"}
