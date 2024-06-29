from pydantic import BaseModel
from typing import List
from .value_objects.id_ingrediente import IdIngrediente
# from .domain_event import DomainEvent

class Ingrediente:
    def __init__(self, _idIngrediente: IdIngrediente, _nombreIngrediente: NombreIngrediente, _cantidadIngrediente: CantidadIngrediente):
        self._idIngrediente = _idIngrediente
        self._nombreIngrediente = _nombreIngrediente
        self._cantidadIngrediente = _cantidadIngrediente
        # eventos: List[DomainEvent]

    @property
    def idIngrediente(self):
        return self._idIngrediente

    @property
    def nombreIngrediente(self):
        return self._nombreIngrediente

    @property
    def cantidadIngrediente(self):
        return self._cantidadIngrediente

    @classmethod
    def create(cls, idIngrediente, nombreIngrediente, cantidadIngrediente):
        return cls(
            idIngrediente=IdIngrediente.create(idIngrediente),
            nombreIngrediente=NombreIngrediente.create(nombreIngrediente),
            cantidadIngrediente=CantidadIngrediente.create(cantidadIngrediente)
        )