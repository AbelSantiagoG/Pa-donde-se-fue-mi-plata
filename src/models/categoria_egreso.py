from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship 
from src.config.database import Base

class Categoria_Egreso(Base):    
    __tablename__ = "categorias_egresos"    

    id              = Column(Integer, primary_key=True, autoincrement=True)      
    descripcion     = Column(String(length=60))

    egresos = relationship("Egreso", back_populates="categoria")
