from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.ingresos import Income
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.ingreso import Ingreso as IngresoModel 
from fastapi.encoders import jsonable_encoder

incomes_router = APIRouter(prefix='/incomes', tags=['incomes'])

def get_all_incomes(incomes) :
    db= SessionLocal()    
    query = db.query(IngresoModel)
    result = query.all()
    return JSONResponse(jsonable_encoder(result), status_code=status.HTTP_200_OK)

def get_income_by_id(id,incomes):
    db = SessionLocal()    
    element = db.query(IngresoModel).filter(IngresoModel.id == id).first()    
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

def create_new_income(ingreso:Income = Body()):
    db = SessionLocal()    
    new_egress = IngresoModel(**ingreso.model_dump())    
    db.add(new_egress)
    db.commit()    
    return JSONResponse(
        content={        
        "message": "The income was successfully created",        
        "data": ingreso.model_dump()    
        }, 
        status_code=status.HTTP_201_CREATED
    ) 

def delete_income(id: int = Path(ge=1)):
    db = SessionLocal()    
    element = db.query(IngresoModel).filter(IngresoModel.id == id).first()    
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested income was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    db.delete(element)    
    db.commit()    
    return JSONResponse(
        content={        
            "message": "The income wass removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

#CRUD ingresos

@incomes_router.get('',response_model=List[Income],description="Returns all incomes")
def get_incomes():
    return get_all_incomes()

@incomes_router.get('{id}',response_model=Income,description="Returns data of one specific income")
def get_income(id: int ) -> Income:
    return get_income_by_id(id)

@incomes_router.post('',response_model=dict,description="Creates a new income")
def create_income(ingreso: Income = Body()):
    return create_new_income(ingreso)

@incomes_router.delete('{id}',response_model=dict,description="Removes specific income")
def remove_income(id: int = Path(ge=1)) -> dict:
    return delete_income(id)
