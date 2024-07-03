from abc import ABC, abstractmethod
from ..platillo import Platillo

class PlatilloInterfazRepositorio(ABC):

    @abstractmethod
    def insertar(self, platillo: Platillo):
        pass