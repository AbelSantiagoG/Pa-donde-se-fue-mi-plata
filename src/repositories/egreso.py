from typing import List
from src.schemas.egresos import Egresos
from src.models.egreso import Egreso as EgresoModel

from sqlalchemy import func

class EgresoRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_egress(self) -> List[Egresos]: 
        query = self.db.query(EgresoModel)
        return query.all()
    
    def get_egreso_by_id(self, id: int ):
        element = self.db.query(EgresoModel).filter(EgresoModel.id == id).first()    
        return element

    def delete_egreso(self, id: int ) -> dict: 
        element: Egresos= self.db.query(EgresoModel).filter(EgresoModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_egress(self, egress:Egresos ) -> dict:
        new_egress = EgresoModel(**egress.model_dump())    
        self.db.add(new_egress)
        self.db.commit()    
        self.db.refresh(new_egress)
        return new_egress
    
    def suma_all_egress(self) -> float: 
        total = self.db.query(func.sum(EgresoModel.value)).scalar()
        return total or 0.0
    
    def get_egress_by_category(self, category:int) -> List[Egresos]:
        query = self.db.query(EgresoModel).filter(EgresoModel.categoria == category)
        return query.all()

