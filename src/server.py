from fastapi import FastAPI, Depends
from src.schema.schema import Product, User
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.infra.sqlalchemy.repositories.user import UserRepository
from src.infra.sqlalchemy.config.database import get_db, create_db

app = FastAPI()
create_db()


@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    created_product = ProductRepository(db).create(product)
    return create_product


@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    # sourcery skip: inline-immediately-returned-variable
    products = ProductRepository(db).list()
    return products


@app.post("/users")
def create_user(user: User, db: Session = Depends(get_db)):
    created_user = UserRepository(db).create(user)
    return create_user


@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    # sourcery skip: inline-immediately-returned-variable
    users = UserRepository(db).list()
    return users
