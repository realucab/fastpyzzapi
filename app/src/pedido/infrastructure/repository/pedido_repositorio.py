from ...domain.repository.pedido_interfaz_repositorio import PedidoInterfazRepositorio
from ...domain.pedido import Pedido
from ..mapper.pedido_orm_mapper import PedidoOrm
from sqlalchemy.orm import Session
from sqlalchemy import insert
from ..mapper.pedido_platillo_association import pedido_platillo
from uuid import UUID
from ....cliente.infrastructure.mapper.cliente_orm_mapper import ClienteOrm

class PedidoRepositorio(PedidoInterfazRepositorio):
    def __init__(self, db: Session):
        self._db = db

    def insertar(self, pedidoData, current_user: dict):
        user_id = UUID(current_user['id'])

        cliente = self._db.query(ClienteOrm).filter(ClienteOrm.user_id == user_id).one()

        nuevoPedido = Pedido.create(
            idCliente = cliente.id_cliente,
            platillos=pedidoData.platillos,
            totalPedido=pedidoData.total_pedido
        )

        nuevoPedidoOrm = PedidoOrm(
            id_pedido=nuevoPedido.idPedido,
            id_cliente=nuevoPedido.idCliente,
            estado_pedido=nuevoPedido.estadoPedido,
            total_pedido=nuevoPedido.totalPedido.value,
            fecha_pedido=nuevoPedido.fechaPedido
        )

        self._db.add(nuevoPedidoOrm)
        self._db.commit()

        # Insert the Pedido and Platillo ids into the pedido_platillo table
        for platillo_id in nuevoPedido.platillos:
            self._db.execute(insert(pedido_platillo).values(
                pedido_id=nuevoPedidoOrm.id_pedido, platillo_id=platillo_id))

        self._db.commit()

        return nuevoPedido