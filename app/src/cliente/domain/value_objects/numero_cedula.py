class NumeroCedula:
    
    def __init__(self, cedula: int):
        self._cedula = cedula
    
    @property
    def cedula(self):
        return self._cedula
    
    @staticmethod
    def create(cedula: int):
        return NumeroCedula(cedula=cedula)