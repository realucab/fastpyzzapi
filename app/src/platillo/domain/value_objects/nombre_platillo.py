class NombrePlatillo:
    
    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @staticmethod
    def create(nombre: str) -> 'NombrePlatillo':
        return NombrePlatillo(nombre=nombre)