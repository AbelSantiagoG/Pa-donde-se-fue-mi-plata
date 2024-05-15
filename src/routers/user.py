from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.user import User
from src.models.user import User as users
from src.repositories.user import UserRepository

user_router = APIRouter(prefix='/users', tags=['users'])

#CRUD user

@user_router.get('',response_model=List[User],description="devuelve todos los usuarios")
def get_categories()-> List[User]:
    db= SessionLocal()
    result = UserRepository(db).get_all_users()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@user_router.get('/{cedula}',response_model=User,description="devuelve un usuario por cedula")
def get_user_by_id(cedula: str = Path(..., description="Cedula del usuario")) -> User:
    db = SessionLocal()
    element=  UserRepository(db).get_user_by_cedula(cedula)
    if not element:        
        return JSONResponse(
            content={            
                "message": "no se encontro el usuario",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@user_router.post('',response_model=User,description="crea un nuevo usuario")
def create_user(user: User = Body(..., description="Usuario a crear")) -> User:
    if UserRepository(db).get_user_by_email(email=user.email) != None:            
                raise Exception("No puede rey") 
    db = SessionLocal()
    new_user = UserRepository(db).create_new_user(user)
    return JSONResponse(
        content=jsonable_encoder(new_user), 
        status_code=status.HTTP_201_CREATED
    )

@user_router.delete('/{cedula}',description="elimina un usuario")
def delete_user(cedula: str = Path(..., description="Cedula del usuario")) -> User:
    db = SessionLocal()
    element = UserRepository(db).delete_user(cedula)
    if not element:        
        return JSONResponse(
            content={            
                "message": "no se encontro el usuario",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
    )

@user_router.put('/{cedula}',response_model=User,description="actualiza un usuario")
def update_user(cedula: str = Path(..., description="Cedula del usuario"), user: User = Body(..., description="Usuario a actualizar")) -> User:
    db = SessionLocal()
    element = UserRepository(db).update_user(cedula, user)
    if not element:        
        return JSONResponse(
            content={            
                "message": "no se encontro el usuario",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
    )
