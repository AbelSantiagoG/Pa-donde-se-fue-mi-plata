from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import JSONResponse

class Egresos (BaseModel):
    id: Optional[int] = Field(default=None, title="Id del egreso")
    fecha: str = Field(title="Fecha del egreso")
    descripcion: Optional[str] = Field(title="Descripcion del egreso")
    valor: float = Field( le=5000001, lg=100,title="Email of the user") 
    categoria: Optional[int] = Field(title="Password of the user")


def get_all_egresos(egresos) :
    return JSONResponse(content=egresos, status_code=200)

def get_egreso_by_id(id,egresos):
    for egreso in egresos:
        if egreso["id"] == id:
            return JSONResponse(content=egreso, status_code=200)
    return JSONResponse(content={"message":"Not found egreso"},status_code=404)

def create_new_egreso(egreso:Egresos, egresos):
    newEgreso = egreso.model_dump()
    egresos.append(newEgreso)
    return JSONResponse(content={
        "message": "The egreso was created successfully",
        "data": newEgreso
        }, status_code=201) 

def delete_egreso(id, egresos):
    for element in egresos:
        if element['id'] == id:
            egresos.remove(element)
            return JSONResponse(content={"message": "The egreso was removed successfully", "data": None }, status_code=200)
    return JSONResponse(content={ "message": "The egreso does not exists", "data": None }, status_code=404)

