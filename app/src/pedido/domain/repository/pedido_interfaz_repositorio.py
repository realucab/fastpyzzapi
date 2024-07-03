from abc import ABC, abstractmethod
from ..pedido import Pedido

class PedidoInterfazRepositorio(ABC):

    @abstractmethod
    def insertar(self, pedido: Pedido):
        pass