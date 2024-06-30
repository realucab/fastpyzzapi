class NumeroTelefono:
    
    def __init__(self, tlf: int):
        self._tlf = tlf
    
    @property
    def tlf(self):
        return self._tlf
    
    @staticmethod
    def create(tlf: int):
        return NumeroTelefono(tlf=tlf)