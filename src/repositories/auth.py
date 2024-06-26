from fastapi import HTTPException, status 
from src.repositories.user import UserRepository 
from src.config.database import SessionLocal 
from src.auth import auth_handler 
from src.schemas.user import UserLogin as UserLoginSchema 
from src.schemas.user import User as UserCreateSchema

class AuthRepository:    
    def __init__(self) -> None:        
        pass

    def register_user(self,                       
                    user: UserCreateSchema) -> dict:        
            db = SessionLocal()        
            if UserRepository(db).get_user_by_email(email=user.email) != None:            
                raise Exception("Account already exists")        
            hashed_password = auth_handler.hash_password(password=user.password)        
            new_user: UserCreateSchema = UserCreateSchema(   
                cedula= user.cedula,
                name=user.name,             
                email=user.email, 
                password=hashed_password,             
                is_active=True        
            )        
            return UserRepository(db).create_new_user(new_user)

    def login_user(self, user: UserLoginSchema) -> dict:        
        db = SessionLocal()        
        check_user = UserRepository(db).get_user_by_email(email=user.email)        
        print(check_user)
        if check_user is None:            
            return HTTPException(                
                status_code=status.HTTP_401_UNAUTHORIZED,                
                detail="Invalid credentials (1)",            
            )                    
        if not check_user.is_active:            
            return HTTPException(                
                status_code=status.HTTP_401_UNAUTHORIZED,                
                detail="The user is not allowed to log in",            
            )        
        if not auth_handler.verify_password(user.password, check_user.password):            
            return HTTPException(                
                status_code=status.HTTP_401_UNAUTHORIZED,                
                detail="Invalid credentials (2)",            
            )        
        access_token = auth_handler.encode_token(check_user)        
        refresh_token = auth_handler.encode_refresh_token(check_user)        
        return access_token, refresh_token