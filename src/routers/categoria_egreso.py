from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.categoria_egreso import Categoria_Egreso 
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.categoria_egreso import Categoria_Egreso as CategoriaModel 
from fastapi.encoders import jsonable_encoder

categories_egress_router = APIRouter(prefix='/categories-egress', tags=['categories_egress'])

List_categories= [
    {"id": 1, "nombre": "Alimentación"},  
    {"id": 2, "nombre": "Transporte"},
    {"id": 3, "nombre": "Ocio"},  
    {"id": 4, "nombre": "Malcriadas"},
]

def get_all_categorias(list):
    return JSONResponse(content=list, status_code=200)

def delete_categoria(id,list):
    for category in list:
        if category["id"]==id:
            list.remove(category)
            return JSONResponse(content={"message": "Category was removed successfully" }, status_code=200)
        
def create_new_categoria(categoria:Categoria_Egreso, categorias):
    newCategoria = categoria.model_dump()
    categorias.append(newCategoria)
    return JSONResponse(content={
        "message": "Income was created successfully",
        "data": newCategoria
        }, status_code=201)

#CRUD categorías

@categories_egress_router.get('/',response_model=List[Categoria_Egreso],description="Returns all categories")
def get_categories():
    return get_all_categorias(List_categories)

@categories_egress_router.post('/',response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria_Egreso = Body()):
    return create_new_categoria(categorie, List_categories)

@categories_egress_router.delete('/{id}',response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    return delete_categoria(id, List_categories)