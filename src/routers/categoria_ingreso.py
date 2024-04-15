from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from schemas.categoria_ingreso import Categoria_Ingreso
from fastapi import APIRouter
from src.config.database import SessionLocal 
from models.categoria_ingreso import Categoria as CategoriaModel 
from fastapi.encoders import jsonable_encoder

categories_incomes = APIRouter(prefix='/categories-incomes', tags=['categories_incomes'])

List_categories= [
    {"id": 1, "nombre": "Pago de nómina"},  
    {"id": 2, "nombre": "Pago contrato"},
    {"id": 3, "nombre": "Pago de arriendo"},  
    {"id": 4, "nombre": "Mesada"}
]

def get_all_categorias(list):
    return JSONResponse(content=list, status_code=200)

def delete_categoria(id,list):
    for category in list:
        if category["id"]==id:
            list.remove(category)
            return JSONResponse(content={"message": "Category was removed successfully" }, status_code=200)
        
def create_new_categoria(categoria:Categoria_Ingreso, categorias):
    newCategoria = categoria.model_dump()
    categorias.append(newCategoria)
    return JSONResponse(content={
        "message": "Income was created successfully",
        "data": newCategoria
        }, status_code=201)

#CRUD categorías

@categories_incomes.get('/',response_model=List[Categoria_Ingreso],description="Returns all categories")
def get_categories():
    return get_all_categorias(List_categories)

@categories_incomes.post('/',response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria_Ingreso = Body()):
    return create_new_categoria(categorie, List_categories)

@categories_incomes.delete('/{id}',response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    return delete_categoria(id, List_categories)