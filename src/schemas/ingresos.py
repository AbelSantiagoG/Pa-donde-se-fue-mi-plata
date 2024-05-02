from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional


class Income (BaseModel):
    id: Optional[int] = Field(default=None, title="Id del ingreso")
    fecha: str = Field(title="Fecha del ingreso")
    description: Optional[str] = Field(default="Ingreso", title="Descripcion del ingreso")
    value:  float = Field( le=5000001, lg=100, title="Valor del ingreso")
    categoria: Optional[int] = Field(title="Categoría del ingreso") 