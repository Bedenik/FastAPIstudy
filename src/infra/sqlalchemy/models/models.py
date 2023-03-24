from typing import List
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Float)
    inStock = Column("in_stock", Boolean)
    user_id = Column(Integer, ForeignKey("user.id", name="fk_user"))
    user = relationship("User", back_populates="products")


class User(Base):
    __allow_unmapped__ = True
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column("name", String)
    phone = Column("phone", String)
    password = Column("password", String)
    products = relationship("Produto", back_populates="user")


Base.metadata.create_all(bind=engine)
