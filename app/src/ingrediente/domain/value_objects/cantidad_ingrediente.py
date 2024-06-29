from pydantic import BaseModel

class CantidadIngrediente:

    def __init__(self, gramos: float):
        self._gramos = gramos

    @property
    def gramos(self):
        return self._gramos
    
    @staticmethod
    def create(gramos: float):
        return CantidadIngrediente(gramos=gramos)
