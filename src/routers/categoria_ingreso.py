from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.categoria_ingreso import Categoria_Ingreso
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.categoria_ingreso import Categoria_Ingreso as CategoriaIngresoModel 
from fastapi.encoders import jsonable_encoder

categories_incomes_router = APIRouter(prefix='/categories-incomes', tags=['categories_incomes'])

def get_all_categorias():
    db = SessionLocal()    
    query = db.query(CategoriaIngresoModel)
    result = query.all()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

def delete_categoria(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()    
    element = db.query(CategoriaIngresoModel).filter(CategoriaIngresoModel.id == id).first()    
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested categorie was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    db.delete(element)    
    db.commit()    
    return JSONResponse(
        content={        
            "message": "The categorie wass removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

def create_new_categoria(categoria:Categoria_Ingreso = Body()) -> dict:
    db = SessionLocal()    
    new_categorie = CategoriaIngresoModel(**categoria.model_dump())    
    db.add(new_categorie)
    db.commit()    
    return JSONResponse(
        content={        
        "message": "The categorie was successfully created",        
        "data": categoria.model_dump()    
        }, 
        status_code=status.HTTP_201_CREATED
    )

#CRUD categorías

@categories_incomes_router.get('',response_model=List[Categoria_Ingreso],description="Returns all categories")
def get_categories():
    return get_all_categorias()

@categories_incomes_router.post('',response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria_Ingreso = Body()):
    return create_new_categoria(categorie)

@categories_incomes_router.delete('{id}',response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    return delete_categoria(id)