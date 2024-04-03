from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import JSONResponse

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