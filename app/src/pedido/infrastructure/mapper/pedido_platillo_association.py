from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.src.common.infrastructure.sqlalchemy_base import Base

pedido_platillo = Table('pedido_platillo', Base.metadata,
    Column('pedido_id', UUID(as_uuid=True), ForeignKey('pedido.id_pedido')),
    Column('platillo_id', UUID(as_uuid=True), ForeignKey('platillo.id_platillo'))
)