from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional


class User (BaseModel):
    cedula: int = Field(default=None, title="Cédula del usuario")
    name: str = Field(title="Fecha del ingreso")
    lastname: Optional[str] = Field(default="Ingreso", title="Descripcion del ingreso")
    email:  float = Field( le=5000001, lg=100, title="Valor del ingreso")
    categoria: Optional[int] = Field(title="Categoría del ingreso") 