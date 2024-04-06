from collections import defaultdict
from fastapi import FastAPI, Body, Path
from typing import List
from fastapi.responses import JSONResponse
from egresos import Egresos, get_all_egresos, get_egreso_by_id,  create_new_egreso, delete_egreso
from ingresos import Income, get_all_incomes, get_income_by_id, create_new_income, delete_income
from src.routers.categorias import Categoria, create_new_categoria, delete_categoria, get_all_categorias

tags_metadata = [
                {"name": "incomes", "description": "imgresos"}, 
                { "name": "egress", "description": "egresos"}, 
                { "name": "reports", "description": "reportes"},  
                { "name": "categories", "description": "categorias"}
]

app = FastAPI(openapi_tags=tags_metadata)



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

@app.get('/incomes',tags=['incomes'],response_model=List[Income],description="Returns all incomes")
def get_incomes():
    return get_all_incomes(incomes)

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

@app.get('/egress',tags=['egress'],response_model=List[Egresos],description="Returns all egress")
def get_egress():
    return get_all_egresos(egress)

@app.get('/egress/{id}',tags=['egress'],response_model=Egresos,description="Returns data of one specific egress")
def get_egress(id: int ) -> Egresos:
    return get_egreso_by_id(id, egress)

@app.post('/egress',tags=['egress'],response_model=dict,description="Creates a new egress")
def create_egress(egreso: Egresos = Body()):
    return create_new_egreso(egreso, egress)

@app.delete('/egress/{id}',tags=['egress'],response_model=dict,description="Removes specific egress")
def remove_egress(id: int = Path(ge=1)) -> dict:
    return delete_egreso(id, egress)



#REPORTES
@app.get('/basic_report',tags=['reports'], response_model=List, description="Returns the basic report")
def get_basic_report():
    egresos = 0
    ingresos = 0
    for expense in egress:
        egresos+= expense["valor"]
    for income in incomes:
        ingresos+= income["valor"]
    restante = ingresos-egresos
    return JSONResponse(content={
        "Basic report":{
        "Ingresos recibidos": str(ingresos),
        "Egresos realizados": str(egresos),
        "Dinero actual": str(restante)
        }

        },
    status_code=200)

@app.get('/expanded_report',tags=['reports'],response_model=List, description="Returns incomes and expenses by categories")
def get_expanded_report():
    report = {"incomes": [], "egress": []}
    ingresos = {}
    egresos = {}
    for income in ingresos:
        id = income["categoria"]
        if id not in ingresos:
            ingresos[id] = []
        ingresos[id].append(income)
    for id, transaccion in ingresos.items():
        report["incomes"].append({
            "Categoria": id,
            "Ingreso": transaccion
        })
    for egress in egresos:
        id = egress["categoria"]
        if id not in egresos:
            egresos[id] = []
        egresos[id].append(egress)
    for id, transaccion in egresos.items():
        report["egress"].append({
            "Categoria": id,
            "Egreso": transaccion
        })
    return JSONResponse(content=report, status_code=200)