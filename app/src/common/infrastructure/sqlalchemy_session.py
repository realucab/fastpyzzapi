from sqlalchemy.orm import sessionmaker
from .sqlalchemy_engine import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)