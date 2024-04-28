from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.egresos import Egresos
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.egreso import Egreso as EgresoModel 
from fastapi.encoders import jsonable_encoder
from src.repositories.egreso import EgresoRepository

egress_router = APIRouter(prefix='/egress', tags=['egress'])

#CRUD egresos

@egress_router.get('',response_model=List[Egresos],description="Returns all egress")
def get_categories()-> List[Egresos]:
    db= SessionLocal()
    result = EgresoRepository(db).get_all_egress()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@egress_router.get('{id}',response_model=Egresos,description="Returns data of one specific egress")
def get_egress(id: int = Path(ge=1)) -> Egresos:
    db = SessionLocal()
    element=  EgresoRepository(db).get_egreso_by_id(id)
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

@egress_router.post('',response_model=dict,description="Creates a new egress")
def create_categorie(egress: Egresos = Body()) -> dict:
    db= SessionLocal()
    new_egress = EgresoRepository(db).create_new_egress(egress)
    return JSONResponse(
        content={        
        "message": "The egress was successfully created",        
        "data": jsonable_encoder(new_egress)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@egress_router.delete('{id}',response_model=dict,description="Removes specific egress")
def remove_egress(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = EgresoRepository(db).get_egress_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested egress was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    EgresoRepository(db).delete_egreso(element)  
    return JSONResponse(
        content={        
            "message": "The egress was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )