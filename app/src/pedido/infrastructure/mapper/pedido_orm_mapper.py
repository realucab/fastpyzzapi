from sqlalchemy import Column, Float, CheckConstraint, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.src.common.infrastructure.sqlalchemy_base import Base
from ...domain.value_objects.estado_pedido import EstadoPedido

class PedidoOrm(Base):
    
        # Tabla:
        __tablename__ = 'pedido'
    
        # Columnas:
        id_pedido = Column(UUID(as_uuid=True), primary_key=True)
        id_cliente = Column(UUID(as_uuid=True), ForeignKey('cliente.id_cliente'))
        estado_pedido = Column(Enum(EstadoPedido), nullable=False)
        total_pedido = Column(Float, CheckConstraint('total_pedido >= 0'), nullable=False)
          
        # Relaciones:
        clientes = relationship('ClienteOrm', back_populates='pedidos')
        platillos = relationship('PlatilloOrm', secondary='pedido_platillo', back_populates='pedidos')
