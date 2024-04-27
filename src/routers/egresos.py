from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.egresos import Egresos
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.egreso import Egreso as EgresoModel 
from fastapi.encoders import jsonable_encoder

egress_router = APIRouter(prefix='/egress', tags=['egress'])


def get_all_egresos():
    db= SessionLocal()    
    query = db.query(EgresoModel)
    result = query.all()
    return JSONResponse(jsonable_encoder(result), status_code=status.HTTP_200_OK)

def get_egreso_by_id(id: int = Path(ge=1)):
    db = SessionLocal()    
    element = db.query(EgresoModel).filter(EgresoModel.id == id).first()    
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested egress was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

def create_new_egreso(egreso:Egresos = Body()):
    db = SessionLocal()    
    new_egress = EgresoModel(**egreso.model_dump())    
    db.add(new_egress)
    db.commit()    
    return JSONResponse(
        content={        
        "message": "The egress was successfully created",        
        "data": egreso.model_dump()    
        }, 
        status_code=status.HTTP_201_CREATED
    )

def delete_egreso(id: int = Path(ge=1)):
    db = SessionLocal()    
    element = db.query(EgresoModel).filter(EgresoModel.id == id).first()    
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested egress was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    db.delete(element)    
    db.commit()    
    return JSONResponse(
        content={        
            "message": "The egress wass removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )


#CRUD egresos

@egress_router.get('',response_model=List[Egresos],description="Returns all egress")
def get_egress():
    return get_all_egresos()

@egress_router.get('{id}',response_model=Egresos,description="Returns data of one specific egress")
def get_egress(id: int = Path(ge=1)) -> Egresos:
    return get_egreso_by_id(id)

@egress_router.post('',response_model=dict,description="Creates a new egress")
def create_egress(egreso: Egresos = Body()):
    return create_new_egreso(egreso)

@egress_router.delete('{id}',response_model=dict,description="Removes specific egress")
def remove_egress(id: int = Path(ge=1)) -> dict:
    return delete_egreso(id)
