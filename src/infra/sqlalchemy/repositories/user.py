from sqlalchemy.orm import Session
from src.schema import schema
from src.infra.sqlalchemy.models import models


class UserRepository():
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: schema.User):
        db_user = models.User(name=user.name, phone=user.telefone, cpf=user.cpf)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def list(self):
        return self.db.query(models.User).all()

    def get(self):
        pass

    def remove(self):
        pass
