from abc import ABC, abstractmethod
from ..cliente import Cliente

class ClienteInterfazRepositorio(ABC):

    @abstractmethod
    def insertar(self, cliente: Cliente):
        pass