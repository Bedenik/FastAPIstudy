from sqlalchemy.orm import Session
from src.schema import schema
from src.infra.sqlalchemy.models import models
class ProductRepository():
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, product: schema.Product):
        db_product = models.Product(name=product.name,price=product.price,inStock=product.inStock)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
    
    
    def list(self):
        return self.db.query(models.Product).all()
        
        
    def get(self):
        pass
    
    def remove(self):
        pass