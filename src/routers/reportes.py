from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter

from src.config.database import SessionLocal 
from src.repositories.ingreso import IngresoRepository
from src.repositories.egreso import EgresoRepository
from src.repositories.categoria_ingreso import CategoriaIngresoRepository
from src.repositories.categoria_egreso import CategoriaEgresoRepository
from src.repositories.user import UserRepository

from src.models.ingreso import Ingreso
from src.models.egreso import Egreso
from src.models.user import User

reportes_router = APIRouter()

#REPORTES

@reportes_router.get('/basic_report/{cedula}', tags=['reports'], response_model=List, description="Returns the basic report")
def get_basic_report(cedula: str):
    db = SessionLocal()
    user = UserRepository(db).get_user_by_cedula(cedula)
    egresos = EgresoRepository(db).suma_all_egress_by_user(cedula)
    ingresos = IngresoRepository(db).suma_all_incomes_by_user(cedula)
    restante = ingresos - egresos
    return JSONResponse(content={ 
        "Basic report": {
            "Usuario": user.name,
            "Ingresos recibidos": str(ingresos),
            "Egresos realizados": str(egresos),
            "Dinero actual": str(restante)
        }
    },
    status_code=200)

@reportes_router.get('/expanded_report/{cedula}', tags=['reports'], response_model=List, description="Returns the expanded report")
def get_expanded_report(cedula : str):
    db = SessionLocal()
    user = UserRepository(db).get_user_by_cedula(cedula)
    incomes_by_category = IngresoRepository(db).get_incomes_by_category_for_user(cedula)

    diccionary = {
        "Usuario": user.name,
        "ingresos": {category: [income.to_dict() for income in incomes] for category, incomes in incomes_by_category.items()}
    }

    return JSONResponse(content=diccionary, status_code=200)

# @reportes_router.get('/expanded_report/{cedula}', tags=['reports'], response_model=List, description="Returns the expanded report")
# def get_expanded_report(cedula : str):
#     user = repoUser.get_user_by_cedula(cedula)
    
#     egreso_categories = repoCategoriaEgresos.get_all_categorias()
#     ingreso_categories = repoCategoriaIngresos.get_all_categorias()
    
#     diccionary = {
#         "Usuario": user.name,
#         "egresos": {category.id: [] for category in egreso_categories},
#         "ingresos": {category.id: [] for category in ingreso_categories}
#     }
    
#     for category in egreso_categories:
#         expenses = EgresoRepository(db).get_egress_by_category_by_user(category.id, cedula)
#         diccionary["egresos"][category.id] = [Egreso.to_dict() for Egreso in expenses]
        
    
#     for category in ingreso_categories:
#         incomes = repoIngresos.get_ingresos_by_category_by_user(category.id, cedula)
#         diccionary["ingresos"][category.id] = [Ingreso.to_dict() for Ingreso in incomes]
        
#     return JSONResponse(content=diccionary, status_code=200)
