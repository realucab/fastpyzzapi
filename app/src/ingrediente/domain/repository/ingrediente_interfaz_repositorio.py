from abc import ABC, abstractmethod
from ..ingrediente import Ingrediente

class IngredienteInterfazRepositorio(ABC):

    @abstractmethod
    def insertar(self, ingrediente: Ingrediente):
        pass

    '''@abstractmethod
    def traerTodos(self):
        pass'''