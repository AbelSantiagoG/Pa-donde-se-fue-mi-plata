from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter

reportes_router = APIRouter()

""" #REPORTES
@reportes_router.get('/basic_report',tags=['reports'], response_model=List, description="Returns the basic report")
def get_basic_report():
    egresos = 0
    ingresos = 0
    for expense in List_egress:
        egresos+= expense["valor"]
    for income in List_incomes:
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

@reportes_router.get('/expanded_report',tags=['reports'],description="Return expanded report")
def get_expanded_report():
    return expanded_report(List_categories,List_egress, List_incomes) """

def expanded_report(listCategories, listExpense, listIncome):
    diccionary = {category["id"]: [] for category in listCategories}

    for category, valor in diccionary.items():
        for expense in listExpense:
            if category == expense["categoria"]:
                addExpense = {"expense": expense}
                valor.append(addExpense)
        for income in listIncome:
            if category == income["categoria"]:
                addIncome = {"income": income}
                valor.append(addIncome)

    report = change_id_categories(listCategories, diccionary)
    return JSONResponse(content={
        "Expanded report":report
        },
    status_code=200)

def general_report(listExpense, ListIncome):
    totalExpense = 0
    totalIncome = 0
    for expense in listExpense:
        totalExpense +=expense["valor"]
    for income in ListIncome:
        totalIncome+= income["valor"]
    subs = totalIncome-totalExpense
    return JSONResponse(content={
        "General report":{
        "Income": "$" + str(totalIncome),
        "Expense": "$" + str(totalExpense),
        "Substraction": "$" + str(subs)
        }
        },
    status_code=200)

def change_id_categories(categories, diccionary):
    newDict = {}
    # diccionario que mapee los id de las categorÃ­as a sus nombres
    category_id_to_name = {category["id"]: category["nombre"] for category in categories}
    for key, value in diccionary.items():
        #Aqui esta cogiendo el valor de category_id_to_name y lo esta poniendo como llave en el nuevo diccionario y le asigna el valor que tenia antes
        newDict[category_id_to_name[key]] = value
    return newDict
