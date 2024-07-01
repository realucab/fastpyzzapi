class DescripcionPlatillo:
    def __init__(self, descripcion: str):
        self._descripcion = descripcion

    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @staticmethod
    def create(descripcion: str) -> 'DescripcionPlatillo':
        return DescripcionPlatillo(descripcion=descripcion)