from pydantic import BaseModel

class NombreIngrediente(BaseModel):
    _nombre: str

    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @staticmethod
    def create(nombre):
        return NombreIngrediente(nombre)