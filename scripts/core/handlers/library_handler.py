import traceback
from fastapi import Request
from scripts.core.db.mongo_utility import mongo
from schemas.models import User
from scripts.core.logging.logs.logger import logging
from fastapi.templating import Jinja2Templates


Templates = Jinja2Templates(directory="Templates")


async def user_signup(request: Request):
    return Templates.TemplateResponse("signup.html", {"request": request})


async def delete_books(request: Request):
    return Templates.TemplateResponse("delete_book.html", {"request": request})


async def user_login(request: Request):
    return Templates.TemplateResponse("login.html", {"request": request})


async def update_books(request: Request):
    return Templates.TemplateResponse("update_book.html", {"request": request})


async def add_book(request: Request):
    return Templates.TemplateResponse("add_books.html", {"request": request})


async def signup(request: Request):
    data = await request.form()
    user = User(
        username=data["username"],
        password=data["password"],
        email=data["email"]
    )
    mongo.for_insert_one("Anirudh_db", user)
    if user:
        logging.info("Sign up page created successfully")
        return {"message": "Signup Successful"}
    else:
        return{"message": "none"}


async def login(request: Request):
    try:
        data = await request.form()
        username = data["username"]
        password = data["password"]
        find = {"username": username, "password": password}
        user = mongo.for_find_one("Anirudh_db", find)
        if user:
            logging.info("login Success")
            print(find)
            return Templates.TemplateResponse("add_books.html", {"request": request})
        else:
            logging.info("incorrect username or password")
            return {"message": "error"}
    except Exception as e:
        traceback.print_exc()
        return {"error", str(e)}


async def add(request: Request):
    try:
        data = await request.form()
        Book_id = data["Book_id"]
        BookName = data["BookName"]
        AuthorName = data["AuthorName"]
        find = {"BookName": BookName}
        add_book_1 = mongo.for_find_one("Anirudh_db", find)
        if add_book_1:
            logging.info("Already Exist")
            return {"message": "Not possible"}
        else:
            insert = {"Book_id": Book_id, "BookName": BookName, "AuthorName": AuthorName}
            print(insert)
            add_book_2 = mongo.for_insert_one("Anirudh_db", insert)
            if add_book_2:
                logging.info("Added Book Successfully")
                return {"message": "successful"}
            else:
                logging.info("Error")
                return {"message": "error"}
    except Exception as e:
        traceback.print_exc()
        return {"error", str(e)}


async def updated_books(request: Request):
    try:
        data = await request.form()
        Book_id = data["Book_id"]
        AuthorName = data["AuthorName"]
        update = {"Book_id": Book_id}
        set = {"$set": {"AuthorName": AuthorName}}
        user = mongo.for_update_one("Anirudh_db", update, set)
        if user:
            logging.info("updated Successfully")
            print(update)
            return {"message": "successful"}
        else:
            logging.info("Update failed")
            return {"message": "AuthorName not updated"}
    except Exception as e:
        traceback.print_exc()
        return {"error", str(e)}


async def deleted_books(request: Request):
    try:
        data = await request.form()
        Book_id = data["Book_id"]
        BookName = data["BookName"]
        AuthorName = data["AuthorName"]
        find = {"Book_id": Book_id, "BookName": BookName, "AuthorName": AuthorName}
        delete_book = mongo.for_find_one("Anirudh_db", find)
        if delete_book:
            delete = {"Book_id": Book_id}
            mongo.for_delete_one("Anirudh_db", delete)
            logging.info("Book Deleted Successfully")
            print(delete)
            return {"message": "successful"}
        else:
            logging.info("Book Not there")
            return {"message": "Book not food"}
    except Exception as e:
        traceback.print_exc()
        return {"error", str(e)}
