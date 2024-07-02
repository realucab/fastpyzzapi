from app.src.common.infrastructure.sqlalchemy_base import Base
from sqlalchemy import Column, String, UUID, Enum as EnumColumn
from sqlalchemy.orm import relationship
from enum import Enum

class UserRole(Enum):
    SYSADMIN = 'SYSADMIN'
    CLIENTE = 'CLIENTE'
    CHEF = 'CHEF'
    ADMINISTRADOR = 'ADMINISTRADOR'

class UserOrm(Base):

    # Tabla:
    __tablename__ = 'user'

    # Columnas:
    user_id = Column(UUID, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(4096))
    user_role = Column(EnumColumn(UserRole), default=UserRole.CLIENTE, nullable=False)

    # Relaciones:
    clientes = relationship('ClienteOrm', back_populates='users')

