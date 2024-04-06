from pydantic import BaseModel, Field
from typing import Optional
from fastapi import FastAPI, Body, Path
from fastapi.responses import JSONResponse
from typing import List




class Categoria (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la categoria")
    description: str = Field(min_length=4, max_length=50, title="Descripcion de la categoria")


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

@app.get('/categories',tags=['categories'],response_model=List[Categoria],description="Returns all categories")
def get_categories():
    return get_all_categorias(categories)

@app.post('/categories',tags=['categories'],response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria = Body()):
    return create_new_categoria(categorie, categories)

@app.delete('/categories/{id}',tags=['categories'],response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    return delete_categoria(id, categories)