from pydantic import BaseModel
from typing import List
from .value_objects.id_ingrediente import IdIngrediente
from .value_objects.cantidad_ingrediente import CantidadIngrediente
from .value_objects.nombre_ingrediente import NombreIngrediente
from uuid import UUID
# from .domain_event import DomainEvent

#class IngredienteModel(BaseModel):
#    idIngrediente: IdIngrediente
#    nombreIngrediente: NombreIngrediente
#    cantidadIngrediente: CantidadIngrediente

class Ingrediente:

    def __init__(self, idIngrediente: IdIngrediente, nombreIngrediente: NombreIngrediente, cantidadIngrediente: CantidadIngrediente):
        self._idIngrediente = idIngrediente
        self._nombreIngrediente = nombreIngrediente
        self._cantidadIngrediente = cantidadIngrediente
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
    def create(cls, idIngrediente: UUID, nombreIngrediente: str, cantidadIngrediente: float):
        return cls(
            idIngrediente=IdIngrediente.create(idIngrediente),
            nombreIngrediente=NombreIngrediente.create(nombreIngrediente),
            cantidadIngrediente=CantidadIngrediente.create(cantidadIngrediente)
        )
    
    #def to_model(self):
    #    return IngredienteModel(
    #        idIngrediente=self.idIngrediente,
    #        nombreIngrediente=self.nombreIngrediente,
    #        cantidadIngrediente=self.cantidadIngrediente
    #    )