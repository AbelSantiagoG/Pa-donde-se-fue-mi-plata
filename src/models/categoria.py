from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship 
from src.config.database import Base

class Categoria(Base):    
    __tablename__ = "categorias"    

    id              = Column(Integer, primary_key=True, autoincrement=True)      
    descripcion     = Column(String(length=60))

    egresos = relationship("Egreso", back_populates="categorias")
    ingresos = relationship("Ingreso", back_populates="categorias")

