from typing import List
from src.schemas.ingresos import Income
from src.models.ingreso import Ingreso as IngresoModel
from sqlalchemy import func
from typing import Dict

class IngresoRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_incomes(self) -> List[Income]: 
        query = self.db.query(IngresoModel)
        return query.all()
    
    def get_ingreso_by_id(self, id: int ):
        element = self.db.query(IngresoModel).filter(IngresoModel.id == id).first()    
        return element

    def delete_ingreso(self, id: int ) -> dict: 
        element: Income= self.db.query(IngresoModel).filter(IngresoModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()
        return element

    def create_new_ingreso(self, income:Income ) -> dict:
        new_income = IngresoModel(**income.model_dump())    
        self.db.add(new_income)
        self.db.commit()    
        self.db.refresh(new_income)
        return new_income

    def suma_all_incomes_by_user(self, cedula:str) -> float: 
        total = self.db.query(func.sum(IngresoModel.value)).filter(IngresoModel.user_cedula == cedula).scalar()
        return total or 0.0
    
    def get_ingresos_by_category(self, category_id: int) -> List[Income]:
        query = self.db.query(IngresoModel).filter(IngresoModel.categoria_ingreso == category_id)
        return query.all()
    
    def get_all_incomes_by_user(self, cedula: str) -> List[Income]:
        query = self.db.query(IngresoModel).filter(IngresoModel.user_cedula == cedula)
        return query.all()
    
    def get_incomes_by_category_for_user(self, cedula: str) -> Dict[int, List[Income]]:
        categories = self.db.query(IngresoModel.categoria).distinct().filter(IngresoModel.user_cedula == cedula).all()
        incomes_by_category = {}
        for category in categories:
            query = self.db.query(IngresoModel).filter(IngresoModel.categoria == category[0], IngresoModel.user_cedula == cedula)
            incomes_by_category[category[0]] = query.all()
        return incomes_by_category
    
    def get_category_by_user(self, cedula: str) -> List[int]:
        query = self.db.query(IngresoModel.categoria).filter(IngresoModel.user_cedula == cedula)
        return [item[0] for item in query.all()]
    
