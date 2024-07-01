from enum import Enum

class TipoPlatillo(Enum):
    PIZZA = 'PIZZA'
    BEBIDA = 'BEBIDA'
    POSTRE = 'POSTRE'
    INGREDIENTE_EXTRA = 'INGREDIENTE_EXTRA'
    
    @staticmethod
    def create(tipo: str) -> 'TipoPlatillo':
        return TipoPlatillo(tipo)