from fastapi import FastAPI, Body, Path
from src.middlewares.error_handler import ErrorHandler
from src.routers.ingresos import incomes_router
from src.routers.egresos import egress_router
from src.routers.categoria_ingreso import categories_incomes_router
from src.routers.categoria_egreso import categories_egress_router
from src.routers.reportes import reportes_router
from src.config.database import Base, engine

Base.metadata.create_all(bind=engine)

##################################################
#                     Tags                       #

tags_metadata = [
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

app.include_router(router= incomes_router)
app.include_router(router= egress_router)
app.include_router(router= categories_incomes_router)
app.include_router(router= categories_egress_router)
app.include_router(prefix="/reports", router= reportes_router)

#################################################







