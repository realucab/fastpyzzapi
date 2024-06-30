from fastapi import APIRouter, Depends, HTTPException
from app.domain.services import LibraryService
from app.domain.schemas import BookCreate, Book
from app.infrastructure.repositories_impl import SQLAlchemyBookRepository
from app.src.ingrediente.domain.value_objects.id_ingrediente import IdIngrediente
from app.src.ingrediente.domain.value_objects.cantidad_ingrediente import CantidadIngrediente
from app.src.ingrediente.domain.value_objects.nombre_ingrediente import NombreIngrediente
from app.src.ingrediente.domain.ingrediente import Ingrediente#, IngredienteModel
from uuid import uuid4, UUID
from app.src.almacen.domain.almacen import Almacen
from app.src.common.infrastructure.modelos_pydantic import as_pydantic_model


router = APIRouter()

async def get_library_service():
    repository = SQLAlchemyBookRepository()
    return LibraryService(repository)

@router.get("/books/", response_model=list[Book])
async def get_books(library_service: LibraryService = Depends(get_library_service)):
    return library_service.get_all_books()

@router.post("/books/", response_model=Book)
async def add_book(book: BookCreate, library_service: LibraryService = Depends(get_library_service)):
    return library_service.add_book(book)

@router.get("/ingredientes/")
@as_pydantic_model
async def get_ingredient():
    # Create a new Ingrediente every time this function is called
    ingrediente = Ingrediente.create(
        idIngrediente=uuid4(),
        nombreIngrediente="Example Ingredient",
        cantidadIngrediente=100
    )
    return ingrediente#.to_model()

@router.get("/almacen/")
@as_pydantic_model
async def get_almacen():
    # Create a new Almacen
    almacen = Almacen.create(capacidadMaxima=1000.0)

    # Create a few Ingredientes and add them to the Almacen
    for _ in range(3):
        ingrediente = Ingrediente.create(
            idIngrediente=uuid4(),
            nombreIngrediente="Example Ingredient",
            cantidadIngrediente=100.0
        )
        almacen.agregarIngrediente(ingrediente)

    return almacen