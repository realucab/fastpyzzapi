from pydantic import BaseModel

class NumeroTelefono(BaseModel):
    _tlf: int
    
    def __init__(self, tlf: int):
        self._tlf = tlf
    
    @property
    def name(self):
        return self._tlf
    
    @staticmethod
    def create(tlf):
        return NumeroTelefono(tlf)