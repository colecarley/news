from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import *
from database import Database

app = FastAPI()
db = Database()

origins = [ "*" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return db.get_users()

@app.post("/users/create")
async def create_user(user: User):
    db.create_user(user)
    return user

@app.post("/users/update")
async def update_user(user: User):
    return db.update_user(user)

@app.post("/users/delete")
async def delete_user(user: User):
    return db.delete_user(user)

@app.get("/users/emails")
async def get_user_emails():
    return db.get_user_emails()

@app.get("/users/email/{email}")
async def get_user_by_email(email: str):
    return db.get_user_by_email(email)

@app.get("/summarizations/since/{since}")
async def get_summarizations_since(since: int):
    return db.get_summarizations_since(since)

@app.post("/summarizations/create")
async def create_summarization(summarization: Summarization):
    return db.create_summarization(summarization)

@app.get("/categories")
async def get_categories():
    return db.get_categories()

@app.post("/categories/create")
async def create_category(category: Category):
    return db.create_category(category)

@app.post("/categories/update")
async def update_category(category: Category):
    return db.update_category(category)

@app.get("/categories/name/{name}")
async def get_category_by_name(name: str):
    return db.get_category_by_name(name)

@app.get("/summarizations/category/{category}")
async def get_summarizations_by_category(category: str):
    category = db.get_category_by_name(category)
    return db.get_summarizations_by_category(category)

@app.get("/users/categories/{email}")
async def get_user_categories(email: str):
    user = db.get_user_by_email(email)
    return db.get_user_categories(user)
