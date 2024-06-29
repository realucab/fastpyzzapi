from pydantic import BaseModel

class NumeroCedula(BaseModel):
    _cedula: int
    
    def __init__(self, cedula: int):
        self._cedula = cedula
    
    @property
    def name(self):
        return self._cedula
    
    @staticmethod
    def create(cedula):
        return NumeroCedula(cedula)