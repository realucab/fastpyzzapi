class CapacidadMaxima:
    def __init__(self, gramos: float):
        self._gramos = gramos
    
    @property
    def gramos(self) -> float:
        return self._gramos
    
    @staticmethod
    def create(gramos: float) -> 'CapacidadMaxima':
        return CapacidadMaxima(gramos=gramos)