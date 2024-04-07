from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.ingresos import Income
from fastapi import APIRouter


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

