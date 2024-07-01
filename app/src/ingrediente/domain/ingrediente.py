from typing import List
from .value_objects.id_ingrediente import IdIngrediente
from .value_objects.cantidad_ingrediente import CantidadIngrediente
from .value_objects.nombre_ingrediente import NombreIngrediente
from uuid import UUID
from app.src.common.domain.domain_event_interface import DomainEvent

class Ingrediente:

    def __init__(self, idIngrediente: IdIngrediente, nombreIngrediente: NombreIngrediente, cantidadIngrediente: CantidadIngrediente, eventos: List[DomainEvent]):
        self._idIngrediente = idIngrediente
        self._nombreIngrediente = nombreIngrediente
        self._cantidadIngrediente = cantidadIngrediente
        self._eventos = eventos

    @property
    def idIngrediente(self):
        return self._idIngrediente

    @property
    def nombreIngrediente(self):
        return self._nombreIngrediente

    @property
    def cantidadIngrediente(self):
        return self._cantidadIngrediente
    
    @property
    def eventos(self) -> List[DomainEvent]:
        return self._eventos

    @classmethod
    def create(cls, idIngrediente: UUID, nombreIngrediente: str, cantidadIngrediente: float):
        return cls(
            idIngrediente=IdIngrediente.create(idIngrediente),
            nombreIngrediente=NombreIngrediente.create(nombreIngrediente),
            cantidadIngrediente=CantidadIngrediente.create(cantidadIngrediente),
            eventos=[]
        )
    
    def agregarEvento(self, evento: DomainEvent):
        self._eventos.append(evento)
    
    def to_dict(self):
        return {
            'idIngrediente': str(self._idIngrediente.id),
            'nombreIngrediente': self._nombreIngrediente.nombre,
            'cantidadIngrediente': self._cantidadIngrediente.gramos,
            'eventos': [str(evento.eventId) for evento in self._eventos]
        }
    