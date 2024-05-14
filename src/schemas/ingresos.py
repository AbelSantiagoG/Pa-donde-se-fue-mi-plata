from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional


class Income (BaseModel):
    id: Optional[int] = Field(default=None, title="Id del ingreso")
    fecha: str = Field(title="Fecha del ingreso")
    description: Optional[str] = Field(default="Ingreso", title="Descripcion del ingreso")
    value:  float = Field( ge=4, le=5000001, title="Valor del ingreso")
    categoria: Optional[int] = Field(title="Categoría del ingreso") 
    user_cedula: str = Field(title="Cedula del usuario")

    @validator('value')
    def value_must_be_positive(cls, v):
        assert isinstance(v, float) and v > 0, "El valor debe ser positivo"
        return v
    
    @validator('description')
    def description_must_contain_space(cls, v):
        assert isinstance(v, str), "La descripcion debe ser un string"
        return v
    
    @validator('fecha')
    def fecha_must_contain_slash(cls, v):
        assert isinstance(v, str) and "-" in v, "La fecha debe contener un -"
        return v
    
    @validator('categoria')
    def categoria_must_be_positive(cls, v):
        assert isinstance(v, int) and v > 0, "La categoria debe ser positiva"
        return v
    
    @validator('user_cedula')
    def user_id_must_contain_space(cls, v):
        assert isinstance(v, str), "La cedula debe ser un string"
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "fecha": "2024-10-10",
                "description": "Salario",
                "value": 1000.0,
                "categoria": 1,
                "user_cedula": "123456789"
            }
        }