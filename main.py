from fastapi import FastAPI, Body, Path
from typing import List
from egresos import Egresos, get_all_egresos, get_egreso_by_id,  create_new_egreso, delete_egreso
from ingresos import Income, get_all_incomes, get_income_by_id, create_new_income, delete_income

tags_metadata = [{"name": "incomes", "description": "imgresos"}  ,  { "name": "egress", "description": "egresos"},]

app = FastAPI(openapi_tags=tags_metadata)

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

egress= [
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

#CRUD ingresos

@app.get('/incomes',tags=['incomes'],response_model=List[incomes],description="Returns all incomes")
def get_incomes():
    return get_all_incomes(Income)

@app.get('/incomes/{id}',tags=['incomes'],response_model=Income,description="Returns data of one specific income")
def get_income(id: int ) -> Income:
    return get_income_by_id(id, incomes)

@app.post('/incomes',tags=['incomes'],response_model=dict,description="Creates a new income")
def create_income(ingreso: Income = Body()):
    return create_new_income(ingreso, incomes)

@app.delete('/incomes/{id}',tags=['incomes'],response_model=dict,description="Removes specific income")
def remove_income(id: int = Path(ge=1)) -> dict:
    return delete_income(id, incomes)

#CRUD egresos

@app.get('/egress',tags=['egress'],response_model=List[incomes],description="Returns all egress")
def get_egress():
    return get_all_egresos(Egresos)

@app.get('/egress/{id}',tags=['egress'],response_model=Income,description="Returns data of one specific egress")
def get_egress(id: int ) -> Egresos:
    return get_egreso_by_id(id, egress)

@app.post('/egress',tags=['egress'],response_model=dict,description="Creates a new egress")
def create_egress(egreso: Egresos = Body()):
    return create_new_egreso(egreso, egress)

@app.delete('/egress/{id}',tags=['egress'],response_model=dict,description="Removes specific egress")
def remove_egress(id: int = Path(ge=1)) -> dict:
    return delete_egreso(id, egress)