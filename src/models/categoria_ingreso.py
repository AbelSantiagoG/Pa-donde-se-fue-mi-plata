from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship 
from src.config.database import Base

class Categoria_Ingreso(Base):    
    __tablename__ = "categorias_ingresos"    

    id              = Column(Integer, primary_key=True, autoincrement=True)      
    description     = Column(String(length=200))

    ingresos = relationship("Ingreso", back_populates="categoria_ingreso")

