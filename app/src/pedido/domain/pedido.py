from typing import List
from uuid import UUID

from app.src.cliente.domain.value_objects.id_cliente import IdCliente
from app.src.platillo.domain.value_objects.id_platillo import IdPlatillo
from .value_objects.id_pedido import IdPedido
from .value_objects.estado_pedido import EstadoPedido
from .value_objects.total_pedido import TotalPedido
from app.src.common.domain.domain_event_abc import DomainEvent

class Pedido:
    def __init__(self, idPedido: IdPedido, idCliente: IdCliente, platillos: List[IdPlatillo], estadoPedido: EstadoPedido, totalPedido: TotalPedido, eventos: List[DomainEvent]):
        self._idPedido = idPedido
        self._idCliente = idCliente
        self._platillos = platillos
        self._estadoPedido = estadoPedido
        self._totalPedido = totalPedido
        self._eventos = eventos

    @property
    def idPedido(self) -> IdPedido:
        return self._idPedido
    
    @property
    def idCliente(self) -> IdCliente:
        return self._idCliente
    
    @property
    def platillos(self) -> List[IdPlatillo]:
        return self._platillos
    
    @property
    def estadoPedido(self) -> EstadoPedido:
        return self._estadoPedido
    
    @property
    def totalPedido(self) -> TotalPedido:
        return self._totalPedido
    
    @property
    def eventos(self) -> List[DomainEvent]:
        return self._eventos
    
    @classmethod
    def create(cls, idPedido: UUID, idCliente: IdCliente, platillos: List[IdPlatillo], estadoPedido: str, totalPedido: float) -> 'Pedido':
        return cls(
            idPedido=IdPedido.create(idPedido),
            idCliente=idCliente,
            platillos=platillos,
            estadoPedido=EstadoPedido.create(estadoPedido),
            totalPedido=TotalPedido.create(totalPedido),
            eventos=[]
        )
    
    def agregarPlatillo(self, platillo: IdPlatillo):
        self._platillos.append(platillo)

    def agregarEvento(self, evento: DomainEvent):
        self.eventos.append(evento)

    def to_dict(self):
        return {
            'idPedido': str(self._idPedido.id),
            'idCliente': str(self._idCliente),
            'platillos': [str(platillo.id) for platillo in self._platillos],
            'estadoPedido': self._estadoPedido.value,
            'totalPedido': self._totalPedido.value,
            'eventos': [str(evento.eventoId) for evento in self.eventos]
        }