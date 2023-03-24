#Schema de api = dados trafegados entre Request e response
from pydantic import BaseModel
from typing import Optional, List

class Product(BaseModel):
    id: Optional[str] = None 
    name: str
    price: float 
    inStock: bool = False 
    class Config:
        orm_mode = True


class User(BaseModel):
    id: Optional[str] = None 
    name: str
    telefone: str 
    password: str
   # products: List[products] = []
   


class PurchaseRequest(BaseModel):
    id: Optional[str] = None 
    product: Product
    user: User
    quantity: int
    delivery: bool = True
    addres: str
