from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.ingresos import Income
from fastapi import APIRouter

incomes= [
    {
        "id": 1,
        "Fecha": "2024-04-02",
        "descripcion": "se ingresó plata",
        "valor":  13.69,
        "categoria": 1
    },
    {
        "id": 2,
        "Fecha": "2024-04-02",
        "descripcion": "se ingresó plata",
        "valor":  12.99,
        "categoria": 2
    }
]

incomes_router = APIRouter()

def get_all_incomes(incomes) :
    return JSONResponse(content=incomes, status_code=200)

def get_income_by_id(id,incomes):
    for element in incomes:
        if element["id"] == id:
            return JSONResponse(content=element, status_code=200)
    return JSONResponse(content={"message":"Income not found"},status_code=404)

def create_new_income(income:Income, incomes):
    newIncome = income.model_dump()
    incomes.append(newIncome)
    return JSONResponse(content={
        "message": "The user was created successfully",
        "data": newIncome
        }, status_code=201) 

def delete_income(id, incomes):
    for element in incomes:
        if element['id'] == id:
            incomes.remove(element)
            return JSONResponse(content={"message": "The income was removed successfully", "data": None }, status_code=200)
    return JSONResponse(content={ "message": "The income does not exists", "data": None }, status_code=404)

#CRUD ingresos

@incomes_router.get('/incomes',tags=['incomes'],response_model=List[Income],description="Returns all incomes")
def get_incomes():
    return get_all_incomes(incomes)

@incomes_router.get('/incomes/{id}',tags=['incomes'],response_model=Income,description="Returns data of one specific income")
def get_income(id: int ) -> Income:
    return get_income_by_id(id, incomes)

@incomes_router.post('/incomes',tags=['incomes'],response_model=dict,description="Creates a new income")
def create_income(ingreso: Income = Body()):
    return create_new_income(ingreso, incomes)

@incomes_router.delete('/incomes/{id}',tags=['incomes'],response_model=dict,description="Removes specific income")
def remove_income(id: int = Path(ge=1)) -> dict:
    return delete_income(id, incomes)
