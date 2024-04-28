from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.categoria_ingreso import Categoria_Ingreso
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.categoria_ingreso import Categoria_Ingreso as CategoriaIngresoModel 
from fastapi.encoders import jsonable_encoder
from src.repositories.categoria_ingreso import CategoriaIngresoRepository

categories_incomes_router = APIRouter(prefix='/categories-incomes', tags=['categories_incomes'])

#CRUD categorías

@categories_incomes_router.get('',response_model=List[Categoria_Ingreso],description="Returns all categories")
def get_categories()-> List[Categoria_Ingreso]:
    db= SessionLocal()
    result = CategoriaIngresoRepository(db).get_all_categorias()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@categories_incomes_router.post('',response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria_Ingreso = Body()) -> dict:
    db= SessionLocal()
    new_categorie = CategoriaIngresoRepository(db).create_new_categoria(categorie)
    return JSONResponse(
        content={        
        "message": "The categorie was successfully created",        
        "data": jsonable_encoder(new_categorie)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@categories_incomes_router.delete('{id}',response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = CategoriaIngresoRepository(db).get_categorie_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested categorie was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    CategoriaIngresoRepository(db).delete_categoria(element)  
    return JSONResponse(
        content={        
            "message": "The categorie was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )