from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.egresos import Egresos
from fastapi import APIRouter


List_egress= [
    {
        "id": 1,
        "Fecha": "2024-04-02",
        "descripcion": "se egresó plata",
        "valor":  69.13,
        "categoria": 8
    },
    {
        "id": 2,
        "Fecha": "2024-04-02",
        "descripcion": "se egresó plata",
        "valor":  15.9,
        "categoria": 7
    }
]

egress_router = APIRouter()


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


#CRUD egresos

@egress_router.get('/egress',tags=['egress'],response_model=List[Egresos],description="Returns all egress")
def get_egress():
    return get_all_egresos(List_egress)

@egress_router.get('/egress/{id}',tags=['egress'],response_model=Egresos,description="Returns data of one specific egress")
def get_egress(id: int ) -> Egresos:
    return get_egreso_by_id(id, List_egress)

@egress_router.post('/egress',tags=['egress'],response_model=dict,description="Creates a new egress")
def create_egress(egreso: Egresos = Body()):
    return create_new_egreso(egreso, List_egress)

@egress_router.delete('/egress/{id}',tags=['egress'],response_model=dict,description="Removes specific egress")
def remove_egress(id: int = Path(ge=1)) -> dict:
    return delete_egreso(id, List_egress)
