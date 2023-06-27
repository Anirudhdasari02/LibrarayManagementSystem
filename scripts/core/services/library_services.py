from fastapi import Request, APIRouter
from fastapi import FastAPI
from scripts.core.handlers import library_handler
from scripts.constants.app_constant import MyConst

app = FastAPI()
app_router = APIRouter()


@app_router.get(MyConst.signup)
async def user_sign(request: Request):
    try:
        return await library_handler.user_signup(request)
    except Exception as e:
        return{"Error": str(e)}


@app_router.get(MyConst.delete_book)
async def deleted(request: Request):
    try:
        return await library_handler.delete_books(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(MyConst.update_book)
async def updated(request: Request):
    try:
        return await library_handler.update_books(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get(MyConst.add_book)
async def add_books(request: Request):
    try:
        return await library_handler.add_book(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.get("/")
async def user(request: Request):
    try:
        return await library_handler.user_login(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(MyConst.add_book)
async def added(request: Request):
    try:
        return await library_handler.add(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(MyConst.delete_book)
async def deleted_1(request: Request):
    try:
        return await library_handler.deleted_books(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(MyConst.update_book)
async def updated_1(request: Request):
    try:
        return await library_handler.updated_books(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(MyConst.signup)
async def signup_post(request: Request):
    try:
        return await library_handler.signup(request)
    except Exception as e:
        return {"Error": str(e)}


@app_router.post(MyConst.login)
async def login_post(request: Request):
    try:
        return await library_handler.login(request)
    except Exception as e:
        return {"Error": str(e)}
