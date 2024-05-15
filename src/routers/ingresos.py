from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.ingresos import Income
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.ingreso import Ingreso as IngresoModel 
from fastapi.encoders import jsonable_encoder
from src.repositories.ingreso import IngresoRepository
from typing import Annotated 
from fastapi.security import HTTPAuthorizationCredentials 
from fastapi import Depends 
from src.auth.has_access import security
from src.auth import auth_handler

incomes_router = APIRouter(prefix='/incomes', tags=['incomes'])

#CRUD ingresos

@incomes_router.get('',response_model=List[Income],description="Returns all incomes")
def get_categories()-> List[Income]:
    db= SessionLocal()
    result = IngresoRepository(db).get_all_incomes()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@incomes_router.get('/{id}',response_model=Income,description="Returns data of one specific income")
def get_incomes(id: int = Path(ge=1)) -> Income:
    db = SessionLocal()
    element=  IngresoRepository(db).get_ingreso_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested income was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@incomes_router.post('',response_model=dict,description="Creates a new income")
def create_categorie(income: Income = Body()) -> dict:
    db= SessionLocal()
    new_income = IngresoRepository(db).create_new_ingreso(income)
    return JSONResponse(
        content={        
        "message": "The income was successfully created",        
        "data": jsonable_encoder(new_income)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@incomes_router.delete('/{id}',response_model=dict,description="Removes specific income")
def remove_incomes( id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = IngresoRepository(db).get_ingreso_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested income was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    IngresoRepository(db).delete_ingreso(id)  
    return JSONResponse(
        content={        
            "message": "The income was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
    )
