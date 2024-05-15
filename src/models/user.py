from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, inspect
from sqlalchemy.orm import relationship 
from src.config.database import Base

class User(Base):    
    __tablename__ = "users"    

    cedula          = Column(String(length=15), primary_key=True)  
    name            = Column(String(length=100))    
    email           = Column(String(length=150))   
    password        = Column(String(length=150))
    is_active       = Column(Boolean, default=True)

    ingresos        = relationship("Ingreso", back_populates="users")
    egresos         = relationship("Egreso", back_populates="users")
    
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
