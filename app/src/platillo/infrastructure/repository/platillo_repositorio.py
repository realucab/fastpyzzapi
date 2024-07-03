from ...domain.repository.platillo_interfaz_repositorio import PlatilloInterfazRepositorio
from ...domain.platillo import Platillo
from ..mapper.platillo_orm_mapper import PlatilloOrm
from sqlalchemy.orm import Session
from sqlalchemy import insert
from ..mapper.platillo_ingrediente_association import platillo_ingrediente

class PlatilloRepositorio(PlatilloInterfazRepositorio):
    def __init__(self, db: Session):
        self._db = db

    def insertar(self, platilloData):
        nuevoPlatillo = Platillo.create(
            nombrePlatillo=platilloData.nombre_platillo,
            precioPlatillo=platilloData.precio_platillo,
            descripcionPlatillo=platilloData.descripcion_platillo,
            tipoPlatillo=platilloData.tipo_platillo,
            ingredientesPlatillo=platilloData.ingredientes_platillo
        )

        nuevoPlatilloOrm = PlatilloOrm(
            id_platillo=nuevoPlatillo.idPlatillo,
            nombre_platillo=nuevoPlatillo.nombrePlatillo.nombre,
            precio_platillo=nuevoPlatillo.precioPlatillo.precio,
            descripcion_platillo=nuevoPlatillo.descripcionPlatillo.descripcion,
            tipo_platillo=nuevoPlatillo.tipoPlatillo
        )

        self._db.add(nuevoPlatilloOrm)
        self._db.commit()

        # Insert the Platillo and Ingrediente ids into the platillo_ingrediente table
        for ingrediente_id in nuevoPlatillo.ingredientesPlatillo:
            self._db.execute(insert(platillo_ingrediente).values(
                platillo_id=nuevoPlatilloOrm.id_platillo, ingrediente_id=ingrediente_id))

        self._db.commit()

        return nuevoPlatillo