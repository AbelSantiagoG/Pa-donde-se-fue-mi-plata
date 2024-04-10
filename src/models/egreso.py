from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship 
from src.config.database import Base

class Egreso(Base):    
    __tablename__ = "egresos"    

    id              = Column(Integer, primary_key=True, autoincrement=True)    
    fecha           = Column(Date)    
    descripcion     = Column(String(length=150))    
    password        = Column(String(length=64))    
    valor           = Column(Integer)
    categoria = relationship("Category", back_populates="egresos") 