from abc import ABC, abstractmethod
from ..ingrediente import Ingrediente

# Nada implementado todavía

class IngredienteInterfazRepositorio(ABC):

    @abstractmethod
    def insertar(self, ingrediente: Ingrediente):
        pass