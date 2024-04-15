from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from schemas.categoria_ingreso import Categoria
from fastapi import APIRouter
from src.config.database import SessionLocal 
from models.categoria_ingreso import Categoria as CategoriaModel 
from fastapi.encoders import jsonable_encoder

categories_egress = APIRouter(prefix='/categories-egress', tags=['categories_egress'])

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
        
def create_new_categoria(categoria:Categoria, categorias):
    newCategoria = categoria.model_dump()
    categorias.append(newCategoria)
    return JSONResponse(content={
        "message": "Income was created successfully",
        "data": newCategoria
        }, status_code=201)

#CRUD categorías

@categories_egress.get('/',response_model=List[Categoria],description="Returns all categories")
def get_categories():
    return get_all_categorias(List_categories)

@categories_egress.post('/',response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria = Body()):
    return create_new_categoria(categorie, List_categories)

@categories_egress.delete('/{id}',response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    return delete_categoria(id, List_categories)