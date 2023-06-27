import uvicorn
from fastapi import FastAPI
from scripts.core.services.library_services import app_router


app = FastAPI()
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
