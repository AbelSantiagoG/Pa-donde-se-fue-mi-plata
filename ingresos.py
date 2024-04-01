from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import JSONResponse

class Income (BaseModel):
    id: Optional[int] = Field(default=None, title="Id del ingreso")
    Fecha: str = Field(title="Fecha del ingreso")
    descripcion: Optional[str] = Field(default="Ingreso", title="Descripcion del ingreso")
    valor:  float = Field( le=5000001, lg=100, title="Valor del ingreso")
    categoria: Optional[int] = Field(title="Categoría del ingreso") 


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
