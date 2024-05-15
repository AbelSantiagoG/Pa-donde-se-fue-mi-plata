from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional


class User (BaseModel):
    cedula: str = Field(min_length=4, title="Cedula del usuario", max_length=15)
    name: str = Field(min_length=3, title="Nombre del usuario", max_length=100)
    email: EmailStr = Field(min_length=4, title="Email del usuario", max_length=150)
    password: str = Field(min_length=8, title="Contraseña del usuario", max_length=150)
    is_active: Optional[bool] = Field(default=True, title="Status of the user")

    @validator("email")
    def email_validator(cls, email):
        assert "@" in email and isinstance (email, str), "Email invalido"
        return email
    
    @validator("password")
    def password_validator(cls, password):
        assert len(password) >= 8, "La contraseña debe tener al menos 8 caracteres"
        return password
    
    @validator("name")
    def name_validator(cls, name):
        assert len(name) >= 3, "El nombre debe tener al menos 3 caracteres"
        return name
    
    @validator("cedula")
    def cedula_validator(cls, cedula):
        assert isinstance(cedula, str) and len(cedula) >= 4, "La cedula debe tener al menos 4 caracteres"
        return cedula

    class Config:
        json_schema_extra = {
            "example": {
                "cedula": "123456789",
                "name": "Miguel",
                "email": "miguel@gmail.com",
                "password": "12345678"
            }
        }

class UserLogin (BaseModel):    
    email: EmailStr = Field(min_length=4, max_length=150, alias="username", title="Email of the user")    
    password: str = Field(min_length=8, title="Contraseña del usuario", max_length=150)