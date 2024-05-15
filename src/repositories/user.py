from typing import List
from src.schemas.user import User as UserSchema
from src.models.user import User as users

class UserRepository:
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_users(self) -> List[UserSchema]:
        query = self.db.query(users)
        return query.all()
    
    def get_user_by_email(self, email: str) -> UserSchema:
        query = self.db.query(users).filter(users.email == email)
        return query.first()
    
    def get_user_by_cedula(self, cedula: str) -> UserSchema:
        query = self.db.query(users).filter(users.cedula == cedula)
        return query.first()
    
    def delete_user(self, cedula: str) -> dict:
        element = self.db.query(users).filter(users.cedula == cedula).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_user(self, user:UserSchema ) -> dict:   
        new_user = users(**user.model_dump())
        self.db.add(new_user)
        
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_user(self, cedula: str, user: UserSchema) -> dict:
        element = self.db.query(users).filter(users.cedula == cedula).first()
        element.name = user.name
        element.email = user.email
        element.password = user.password

        self.db.commit()
        self.db.refresh(element)
        return element