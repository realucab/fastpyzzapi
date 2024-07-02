from app.src.common.infrastructure.sqlalchemy_base import Base
from sqlalchemy import Column, String, UUID

class UserOrm(Base):
    __tablename__ = 'user'

    user_id = Column(UUID, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(4096))