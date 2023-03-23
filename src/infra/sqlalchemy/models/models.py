from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, Integer, String, Float, Boolean,Table, ForeignKey
from src.infra.sqlalchemy.config.database import Base, engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    price = Column('price', Float)
    inStock = Column('in_stock', Boolean)
    
class PurchaseRequest(Base):
    
    __tablename__ = 'purchaseRequest'
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    user = List['User']
    quantity = Column(Integer)
    delivery = Column(Boolean)
    address = Column(String)

    
class User(Base):
    __allow_unmapped__= True
    __tablename__ = 'user'
    
    id: Column(Integer, primary_key=True, index=True)
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    phone = Column('phone', String)
    cpf = Column('cpf', String)

Base.metadata.create_all(bind=engine)



    

    
