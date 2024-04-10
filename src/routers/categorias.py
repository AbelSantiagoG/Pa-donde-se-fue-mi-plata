from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.categorias import Categoria
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.categoria import Categoria as CategoriaModel 
from fastapi.encoders import jsonable_encoder

categories_router = APIRouter()

List_categories= [
    {"id": 1, "nombre": "Pago de nómina"},  
    {"id": 2, "nombre": "Pago contrato"},
    {"id": 3, "nombre": "Pago de arriendo"},  
    {"id": 4, "nombre": "Mesada"},
    {"id": 5, "nombre": "Alimentación"},  
    {"id": 6, "nombre": "Transporte"},
    {"id": 7, "nombre": "Ocio"},  
    {"id": 8, "nombre": "Malcriadas"},
]

def get_all_categorias(list):
    return JSONResponse(content=list, status_code=200)

def delete_categoria(id,list):
    for category in list:
        if category["id"]==id:
            list.remove(category)
            return JSONResponse(content={"message": "Category was removed successfully" }, status_code=200)
        
def create_new_categoria(categoria:Categoria, categorias):
    newCategoria = categoria.model_dump()
    categorias.append(newCategoria)
    return JSONResponse(content={
        "message": "Income was created successfully",
        "data": newCategoria
        }, status_code=201)

#CRUD categorías

@categories_router.get('/categories',tags=['categories'],response_model=List[Categoria],description="Returns all categories")
def get_categories():
    return get_all_categorias(List_categories)

@categories_router.post('/categories',tags=['categories'],response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria = Body()):
    return create_new_categoria(categorie, List_categories)

@categories_router.delete('/categories/{id}',tags=['categories'],response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    return delete_categoria(id, List_categories)