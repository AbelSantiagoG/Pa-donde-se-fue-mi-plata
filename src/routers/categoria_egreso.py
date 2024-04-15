from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.categoria_egreso import Categoria_Egreso 
from fastapi import APIRouter
from src.config.database import SessionLocal 
from src.models.categoria_egreso import Categoria_Egreso as CategoriaEgresoModel 
from fastapi.encoders import jsonable_encoder

categories_egress_router = APIRouter(tags=['categories_egress'])


def get_all_categorias():
    db = SessionLocal()    
    query = db.query(CategoriaEgresoModel)
    result = query.all()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

def delete_categoria(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()    
    element = db.query(CategoriaEgresoModel).filter(CategoriaEgresoModel.id == id).first()    
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested categorie was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    db.delete(element)    
    db.commit()    
    return JSONResponse(
        content={        
            "message": "The categorie wass removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

def create_new_categoria(categoria:Categoria_Egreso = Body()) -> dict:
    db = SessionLocal()    
    new_categorie = CategoriaEgresoModel(**categoria.model_dump())    
    db.add(new_categorie)
    db.commit()    
    return JSONResponse(
        content={        
        "message": "The categorie was successfully created",        
        "data": categoria.model_dump()    
        }, 
        status_code=status.HTTP_201_CREATED
    )

#CRUD categorías

@categories_egress_router.get('/categories-egress',response_model=List[Categoria_Egreso],description="Returns all categories")
def get_categories():
    return get_all_categorias()

@categories_egress_router.post('/categories-egress',response_model=dict,description="Creates a new categorie")
def create_categorie(categorie: Categoria_Egreso = Body()):
    return create_new_categoria(categorie)

@categories_egress_router.delete('/categories-egress{id}',response_model=dict,description="Removes specific categorie")
def remove_categorie(id: int = Path(ge=1)) -> dict:
    return delete_categoria(id)