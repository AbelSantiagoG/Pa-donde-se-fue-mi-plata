from typing import List
from src.schemas.categoria_egreso import Categoria_Egreso
from src.models.categoria_egreso import Categoria_Egreso as CategoriaModel

class CategoriaEgresoRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_categorias(self) -> List[Categoria_Egreso]: 
        query = self.db.query(CategoriaModel)
        return query.all()
    
    def get_categorie_by_id(self, id: int ):
        element = self.db.query(CategoriaModel).filter(CategoriaModel.id == id).first()    
        return element
    
    def delete_categoria(self, id: int ) -> dict: 
        element: Categoria_Egreso= self.db.query(CategoriaModel).filter(CategoriaModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_categoria(self, categoria:Categoria_Egreso ) -> dict:
        new_categorie = CategoriaModel(**categoria.model_dump())    
        self.db.add(new_categorie)
        self.db.commit()    
        self.db.refresh(new_categorie)
        return new_categorie