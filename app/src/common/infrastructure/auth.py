import os
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from .sqlalchemy_session import get_db
from ...usuario.infrastructure.mapper.usuario_orm_mapper import UserOrm
from .custom_bcrypt import bcrypt as bcrypt_context
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from uuid import uuid4, UUID
import logging

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    hashed_password = bcrypt_context.hashpw(create_user_request.password.encode(), bcrypt_context.gensalt())
    create_user_model = UserOrm(
        user_id=uuid4(),
        username=create_user_request.username,
        hashed_password=hashed_password
    )

    db.add(create_user_model)
    db.commit()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user.'
        )
    access_token = create_access_token(user.username, str(user.user_id), timedelta(minutes=20)) # Evaluar si se puede extender
    return {"access_token": access_token, "token_type": "bearer"}

def authenticate_user(username: str, password: str, db):
    user = db.query(UserOrm).filter(UserOrm.username == username).first()
    if not user:
        return False
    if not bcrypt_context.checkpw(password.encode(), user.hashed_password.encode()):
        return False
    return user

def create_access_token(username: str, user_id: str, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    logger.info("Resolving user_dependency")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: UUID = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate user.'
            )
        logger.info("Resolved user_dependency")
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user.'
        )

user_dependency = Annotated[dict, Depends(get_current_user)]


