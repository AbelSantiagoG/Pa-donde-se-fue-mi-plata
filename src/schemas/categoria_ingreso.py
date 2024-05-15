from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class Categoria_Ingreso (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la categoria")
    description: str = Field(min_length=4, max_length=50, title="Descripcion de la categoria")

    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "description": "Trabajo"
            }
        }