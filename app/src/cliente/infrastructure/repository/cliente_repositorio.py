from ...domain.repository.cliente_interfaz_repositorio import ClienteInterfazRepositorio
from ...domain.cliente import Cliente
from ..mapper.cliente_orm_mapper import ClienteOrm
from sqlalchemy.orm import Session
from uuid import UUID

class ClienteRepositorio(ClienteInterfazRepositorio):
    def __init__(self, db: Session):
        self._db = db

    def insertar(self, clienteData, current_user: dict):
        user_id = UUID(current_user['id'])

        nuevoCliente = Cliente.create(
            nombreCliente=clienteData.nombre_cliente,
            numeroCedula=clienteData.numero_cedula,
            emailCliente=clienteData.email_cliente,
            numeroTelefono=clienteData.numero_telefono
        )

        nuevoClienteOrm = ClienteOrm(
            id_cliente=nuevoCliente.idCliente,
            nombre_cliente=nuevoCliente.nombreCliente.nombre,
            numero_cedula=nuevoCliente.numeroCedula.cedula,
            email_cliente=nuevoCliente.emailCliente.email,
            numero_telefono=nuevoCliente.numeroTelefono.tlf,
            user_id=user_id
        )

        self._db.add(nuevoClienteOrm)
        self._db.commit()

        return nuevoCliente