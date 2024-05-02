from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, inspect
from sqlalchemy.orm import relationship 
from src.config.database import Base

class Egreso(Base):    
    __tablename__ = "egresos"    

    id              = Column(Integer, primary_key=True, autoincrement=True)    
    fecha           = Column(Date)    
    description     = Column(String(length=150))    
    value           = Column(Integer)
    categoria       = Column(Integer, ForeignKey("categorias_egresos.id"))

    categoria_egreso      = relationship("Categoria_Egreso", back_populates="egresos") 
    
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}