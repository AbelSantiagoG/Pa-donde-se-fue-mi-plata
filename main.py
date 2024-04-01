from fastapi import FastAPI, Body, Path
from typing import List

tags_metadata = [{"name": "web", "description": "Endpoints of example"}  ,  { "name": "users", "description": "User handling endpoints"},]

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

incomes= [ ]

egress= [ ]