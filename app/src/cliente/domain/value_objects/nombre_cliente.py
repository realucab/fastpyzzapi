from pydantic import BaseModel

class NombreCliente(BaseModel):
    _nombre: str
    
    def __init__(self, nombre: str):
        self._nombre = nombre
    
    @property
    def name(self):
        return self._nombre
    
    @staticmethod
    def create(nombre):
        return NombreCliente(nombre)