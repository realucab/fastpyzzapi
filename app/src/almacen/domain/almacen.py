from typing import List
from app.src.ingrediente.domain.ingrediente import Ingrediente
from .value_objects.capacidad_maxima import CapacidadMaxima

class Almacen:
    def __init__(self, capacidadMaxima: CapacidadMaxima, ingredientesAlmacen: List[Ingrediente]):
        self._capacidadMaxima = capacidadMaxima
        self._ingredientesAlmacen = ingredientesAlmacen

    @property
    def capacidadAlmacen(self) -> CapacidadMaxima:
        return self._capacidadMaxima

    @property
    def ingredientes(self) -> List[Ingrediente]:
        return self._ingredientesAlmacen

    @classmethod
    def create(cls, capacidadMaxima: float) -> 'Almacen':
        return cls(
            capacidadMaxima=CapacidadMaxima.create(capacidadMaxima),
            ingredientesAlmacen=[]
        )
    
    def agregarIngrediente(self, ingrediente: Ingrediente):
        self._ingredientesAlmacen.append(ingrediente)

    def to_dict(self):
        return {
            "capacidadMaxima": self._capacidadMaxima.gramos,
            "ingredientesAlmacen": [str(ingrediente.idIngrediente.id) for ingrediente in self._ingredientesAlmacen]
        }