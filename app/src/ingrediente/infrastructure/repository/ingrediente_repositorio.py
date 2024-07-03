from ...domain.repository.ingrediente_interfaz_repositorio import IngredienteInterfazRepositorio
from ...domain.ingrediente import Ingrediente
from ..mapper.ingrediente_orm_mapper import IngredienteOrm
import logging
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class IngredienteRepositorio(IngredienteInterfazRepositorio):

    def __init__(self, db: Session):
        self._db = db

    def insertar(self, ingredienteData):
        nuevoIngrediente = Ingrediente.create(
            nombreIngrediente=ingredienteData.nombre_ingrediente,
            cantidadIngrediente=ingredienteData.cantidad_ingrediente
        )

        nuevoIngredienteOrm = IngredienteOrm(
            id_ingrediente=nuevoIngrediente.idIngrediente,
            nombre_ingrediente=nuevoIngrediente.nombreIngrediente.nombre,
            cantidad_ingrediente=nuevoIngrediente.cantidadIngrediente.gramos
        )
        logger.info(f"Nuevo ingrediente: {nuevoIngredienteOrm}")

        self._db.add(nuevoIngredienteOrm)
        self._db.commit()

        return nuevoIngrediente