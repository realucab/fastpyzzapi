from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.src.common.infrastructure.sqlalchemy_base import Base

platillo_ingrediente = Table('platillo_ingrediente', Base.metadata,
    Column('platillo_id', UUID(as_uuid=True), ForeignKey('platillo.id_platillo')),
    Column('ingrediente_id', UUID(as_uuid=True), ForeignKey('ingrediente.id_ingrediente'))
)