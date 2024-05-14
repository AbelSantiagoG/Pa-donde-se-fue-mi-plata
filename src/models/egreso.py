from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, inspect, Float
from sqlalchemy.orm import relationship 
from src.config.database import Base

class Egreso(Base):    
    __tablename__ = "egresos"    

    id              = Column(Integer, primary_key=True, autoincrement=True)    
    fecha           = Column(String(length=10))    
    description     = Column(String(length=200))    
    value           = Column(Float)
    categoria       = Column(Integer, ForeignKey("categorias_egresos.id"))
    user_cedula     = Column(String(length=15), ForeignKey("users.cedula"))

    categoria_egreso      = relationship("Categoria_Egreso", back_populates="egresos")
    users                 = relationship("User", back_populates="egresos")
    
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}