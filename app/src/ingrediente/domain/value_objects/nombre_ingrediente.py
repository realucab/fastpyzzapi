class NombreIngrediente:

    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @staticmethod
    def create(nombre: str):
        return NombreIngrediente(nombre=nombre)
