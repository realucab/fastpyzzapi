from pydantic import BaseModel

class NombreCliente():
    
    def __init__(self, nombre: str):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @staticmethod
    def create(nombre: str):
        return NombreCliente(nombre=nombre)