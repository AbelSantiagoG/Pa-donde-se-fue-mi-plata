from fastapi import FastAPI, Body, Path
from src.middlewares.error_handler import ErrorHandler
from src.routers.ingresos import incomes_router
from src.routers.egresos import egress_router
from src.routers.categoria_ingreso import categories_incomes_router
from src.routers.categoria_egreso import categories_egress_router
from src.routers.reportes import reportes_router
from src.routers.user import user_router

from src.models.ingreso import Ingreso
from src.models.egreso import Egreso
from src.models.categoria_ingreso import Categoria_Ingreso
from src.models.categoria_egreso import Categoria_Egreso
from src.models.user import User

from src.config.database import Base, engine

Base.metadata.create_all(bind=engine)

##################################################
#                     Tags                       #

tags_metadata = [
    {"name": "users", "description": "usuarios"},
    {"name": "incomes", "description": "imgresos"}, 
    { "name": "egress", "description": "egresos"}, 
    { "name": "reports", "description": "reportes"},  
    { "name": "categories_incomes", "description": "categorias de los ingresos"},
    { "name": "categories_egress", "description": "categorias de los egresos"}
]

app = FastAPI(openapi_tags=tags_metadata)

#################################################
#                 Middlewares                   #

#app.add_middleware(ErrorHandler)

#################################################
#      Router's definition (endpoints sets)     #

app.include_router(router= user_router)
app.include_router(router= incomes_router)
app.include_router(router= egress_router)
app.include_router(router= categories_incomes_router)
app.include_router(router= categories_egress_router)
app.include_router(prefix="/reports", router= reportes_router)

#################################################







