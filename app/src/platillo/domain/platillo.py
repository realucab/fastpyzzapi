from typing import List
from uuid import UUID

from app.src.ingrediente.domain.value_objects.id_ingrediente import IdIngrediente
from .value_objects.tipo_platillo import TipoPlatillo
from .value_objects.descripcion_platillo import DescripcionPlatillo
from .value_objects.precio_platillo import PrecioPlatillo
from .value_objects.nombre_platillo import NombrePlatillo
from .value_objects.id_platillo import IdPlatillo
from uuid import uuid4

class Platillo:
    def __init__(self, idPlatillo: IdPlatillo, nombrePlatillo: NombrePlatillo, precioPlatillo: PrecioPlatillo, descripcionPlatillo: DescripcionPlatillo, tipoPlatillo: TipoPlatillo, ingredientesPlatillo: List[IdIngrediente]):
        self._idPlatillo = idPlatillo
        self._nombrePlatillo = nombrePlatillo
        self._precioPlatillo = precioPlatillo
        self._descripcionPlatillo = descripcionPlatillo
        self._tipoPlatillo = tipoPlatillo
        self._ingredientesPlatillo = ingredientesPlatillo

    @property
    def idPlatillo(self) -> IdPlatillo:
        return self._idPlatillo

    @property
    def nombrePlatillo(self) -> NombrePlatillo:
        return self._nombrePlatillo

    @property
    def precioPlatillo(self) -> PrecioPlatillo:
        return self._precioPlatillo

    @property
    def descripcionPlatillo(self) -> DescripcionPlatillo:
        return self._descripcionPlatillo

    @property
    def tipoPlatillo(self) -> TipoPlatillo:
        return self._tipoPlatillo

    @property
    def ingredientesPlatillo(self) -> List[IdIngrediente]:
        return self._ingredientesPlatillo

    @classmethod
    def create(cls, nombrePlatillo: str, precioPlatillo: float, descripcionPlatillo: str, tipoPlatillo: str, ingredientesPlatillo: List[IdIngrediente]) -> 'Platillo':
        return cls(
            idPlatillo=uuid4(),
            nombrePlatillo=NombrePlatillo.create(nombrePlatillo),
            precioPlatillo=PrecioPlatillo.create(precioPlatillo),
            descripcionPlatillo=DescripcionPlatillo.create(descripcionPlatillo),
            tipoPlatillo=TipoPlatillo.create(tipoPlatillo),
            ingredientesPlatillo=ingredientesPlatillo
        )
    
    def agregarIngrediente(self, ingrediente: IdIngrediente):
        self._ingredientesPlatillo.append(ingrediente)

    def to_dict(self):
        return {
            'idPlatillo': str(self._idPlatillo),
            'nombrePlatillo': self._nombrePlatillo.nombre,
            'precioPlatillo': self._precioPlatillo.precio,
            'descripcionPlatillo': self._descripcionPlatillo.descripcion,
            'tipoPlatillo': self._tipoPlatillo.value,
            'ingredientesPlatillo': [str(ingrediente) for ingrediente in self._ingredientesPlatillo]
        }