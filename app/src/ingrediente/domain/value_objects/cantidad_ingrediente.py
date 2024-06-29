from pydantic import BaseModel

class CantidadIngrediente(BaseModel):
    _gramos: float

    def __init__(self, gramos: float):
        self._gramos = gramos

    @property
    def gramos(self):
        return self._gramos
    
    @staticmethod
    def create(gramos):
        return CantidadIngrediente(gramos)
