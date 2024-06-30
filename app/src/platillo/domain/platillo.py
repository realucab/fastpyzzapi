from typing import List
from uuid import UUID

from app.src.ingrediente.domain.ingrediente import Ingrediente
from .value_objects.tipo_platillo import TipoPlatillo
from .value_objects.descripcion_platillo import DescripcionPlatillo
from .value_objects.precio_platillo import PrecioPlatillo
from .value_objects.nombre_platillo import NombrePlatillo
from .value_objects.id_platillo import IdPlatillo

class Platillo:
    def __init__(self, idPlatillo: IdPlatillo, nombrePlatillo: NombrePlatillo, precioPlatillo: PrecioPlatillo, descripcionPlatillo: DescripcionPlatillo, tipoPlatillo: TipoPlatillo, ingredientesPlatillo: List[Ingrediente]):
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
    def ingredientesPlatillo(self) -> List[Ingrediente]:
        return self._ingredientesPlatillo

    @classmethod
    def create(cls, idPlatillo: UUID, nombrePlatillo: str, precioPlatillo: float, descripcionPlatillo: str, tipoPlatillo: str, ingredientesPlatillo: List[Ingrediente]) -> 'Platillo':
        return cls(
            idPlatillo=IdPlatillo.create(idPlatillo),
            nombrePlatillo=NombrePlatillo.create(nombrePlatillo),
            precioPlatillo=PrecioPlatillo.create(precioPlatillo),
            descripcionPlatillo=DescripcionPlatillo.create(descripcionPlatillo),
            tipoPlatillo=TipoPlatillo.create(tipoPlatillo),
            ingredientesPlatillo=ingredientesPlatillo
        )
    
    def agregarIngrediente(self, ingrediente: Ingrediente):
        self._ingredientesPlatillo.append(ingrediente)

    def to_dict(self):
        return {
            'idPlatillo': str(self._idPlatillo.id),
            'nombrePlatillo': self._nombrePlatillo.nombre,
            'precioPlatillo': self._precioPlatillo.precio,
            'descripcionPlatillo': self._descripcionPlatillo.descripcion,
            'tipoPlatillo': self._tipoPlatillo.value,
            'ingredientesPlatillo': [str(ingrediente.idIngrediente.id) for ingrediente in self._ingredientesPlatillo]
        }