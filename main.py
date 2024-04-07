from collections import defaultdict
from fastapi import FastAPI, Body, Path
from src.middlewares.error_handler import ErrorHandler
from src.routers.ingresos import incomes_router
from src.routers.egresos import egress_router
from src.routers.categorias import categories_router
from src.routers.reportes import reportes_router


##################################################
#                     Tags                       #

tags_metadata = [
    {"name": "incomes", "description": "imgresos"}, 
    { "name": "egress", "description": "egresos"}, 
    { "name": "reports", "description": "reportes"},  
    { "name": "categories", "description": "categorias"}
]

app = FastAPI(openapi_tags=tags_metadata)

#################################################
#                 Middlewares                   #

app.add_middleware(ErrorHandler)

#################################################
#      Router's definition (endpoints sets)     #

app.include_router(prefix="/incomes", router=incomes_router)
app.include_router(prefix="/egress", router=egress_router)
app.include_router(prefix="/categories", router=categories_router)
app.include_router(prefix="/reports", router=reportes_router)

#################################################







