from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class Egresos (BaseModel):
    id: Optional[int] = Field(default=None, title="Id del egreso")
    fecha: str = Field(title="Fecha del egreso")
    descripcion: Optional[str] = Field(title="Descripcion del egreso")
    valor: float = Field( le=5000001, lg=100,title="Valor del egreso") 
    categoria: Optional[int] = Field(title="Contraseña del egreso")
