from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.categoria_egreso import Categoria_Egreso 
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.categoria_egreso import Categoria_Egreso as CategoriaEgresoModel 
from fastapi.encoders import jsonable_encoder
from src.repositories.categoria_egreso import CategoriaEgresoRepository

categories_egress_router = APIRouter(tags=['categories_egress'])

#CRUD categorías

@categories_egress_router.get('/categories-egress',response_model=List[Categoria_Egreso],description="Returns all categories")
def get_categories()-> List[Categoria_Egreso]:
    db= SessionLocal()
    result = CategoriaEgresoRepository(db).get_all_categorias()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@categories_egress_router.post('/categories-egress',response_model=Categoria_Egreso,description="Creates a new categorie")
def create_categorie(categorie: Categoria_Egreso = Body()) -> dict:
    db= SessionLocal()
    new_categorie = CategoriaEgresoRepository(db).create_new_categoria(categorie)
    return JSONResponse(
        content={        
        "message": "The categorie was successfully created",        
        "data": jsonable_encoder(new_categorie)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@categories_egress_router.delete('/categories-egress{id}',response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = CategoriaEgresoRepository(db).get_categorie_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested categorie was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    CategoriaEgresoRepository(db).delete_categoria(id)  
    return JSONResponse(
        content={        
            "message": "The categorie was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )