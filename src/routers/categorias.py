from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.categorias import Categoria
from fastapi import APIRouter

categories_router = APIRouter()

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

categories= [
    {"id": 1, "description": "Pago de nómina"},  
    {"id": 2, "description": "Pago contrato"},
    {"id": 3, "description": "Pago de arriendo"},  
    {"id": 4, "description": "Mesada"},
    {"id": 5, "description": "Alimentación"},  
    {"id": 6, "description": "Transporte"},
    {"id": 7, "description": "Ocio"},  
    {"id": 8, "description": "Malcriadas"},
    ]

#CRUD categorías

@categories_router.get('/categories',tags=['categories'],response_model=List[Categoria],description="Returns all categories")
def get_categories():
    return get_all_categorias(categories)

@categories_router.post('/categories',tags=['categories'],response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria = Body()):
    return create_new_categoria(categorie, categories)

@categories_router.delete('/categories/{id}',tags=['categories'],response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    return delete_categoria(id, categories)