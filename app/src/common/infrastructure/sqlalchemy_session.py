from sqlalchemy.orm import sessionmaker
from .sqlalchemy_engine import engine

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)