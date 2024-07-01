from fastapi import APIRouter, Depends, HTTPException
from app.domain.services import LibraryService
from app.domain.schemas import BookCreate, Book
from app.infrastructure.repositories_impl import SQLAlchemyBookRepository
from app.src.ingrediente.domain.value_objects.id_ingrediente import IdIngrediente
from app.src.ingrediente.domain.value_objects.cantidad_ingrediente import CantidadIngrediente
from app.src.ingrediente.domain.value_objects.nombre_ingrediente import NombreIngrediente
from app.src.ingrediente.domain.ingrediente import Ingrediente#, IngredienteModel
from app.src.cliente.domain.cliente import Cliente
from uuid import uuid4, UUID
from app.src.almacen.domain.almacen import Almacen
from app.src.common.infrastructure.modelos_pydantic import *
from app.src.platillo.domain.platillo import Platillo
from app.src.pedido.domain.pedido import Pedido


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

@router.get("/ingredientes/", response_model=IngredienteModel)
@as_pydantic_model
async def get_ingredient():
    # Create a new Ingrediente every time this function is called
    ingrediente = Ingrediente.create(
        idIngrediente=uuid4(),
        nombreIngrediente="Example Ingredient",
        cantidadIngrediente=100
    )
    return ingrediente#.to_model()

@router.get("/almacen/", response_model=AlmacenModel)
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
        almacen.agregarIngrediente(ingrediente.idIngrediente)

    return almacen

@router.get("/clientes/", response_model=ClienteModel)
@as_pydantic_model
async def get_client():
    # Create a new Cliente
    cliente = Cliente.create(
        idCliente=uuid4(),
        nombreCliente="Example Client",
        numeroCedula=28101010,
        emailCliente="prueba@example.com",
        numeroTelefono=584145556666
    )
    return cliente

@router.get("/platillos/", response_model=PlatilloModel)
@as_pydantic_model
async def get_platillo():

    ingredientes = []
    for _ in range(3):
        ingrediente = Ingrediente.create(
            idIngrediente=uuid4(),
            nombreIngrediente="Example Ingredient",
            cantidadIngrediente=100.0
        )
        ingredientes.append(ingrediente)

    id_ingredientes = [ingrediente.idIngrediente for ingrediente in ingredientes]

    platillo = Platillo.create(
        idPlatillo=uuid4(),
        nombrePlatillo="Example Platillo",
        precioPlatillo=10.0,
        descripcionPlatillo="This is an example platillo",
        tipoPlatillo="PIZZA",
        ingredientesPlatillo=id_ingredientes
    )

    return platillo

@router.get("/pedidos/", response_model=PedidoModel)
@as_pydantic_model
async def get_platillo():

    ingredientes = []
    for _ in range(3):
        ingrediente = Ingrediente.create(
            idIngrediente=uuid4(),
            nombreIngrediente="Example Ingredient",
            cantidadIngrediente=100.0
        )
        ingredientes.append(ingrediente)

    platillos = [Platillo.create(
        idPlatillo=uuid4(),
        nombrePlatillo="Example Platillo",
        precioPlatillo=10.0,
        descripcionPlatillo="This is an example platillo",
        tipoPlatillo="PIZZA",
        ingredientesPlatillo=ingredientes
    )]

    id_platillos = [platillo.idPlatillo for platillo in platillos]

    cliente = Cliente.create(
        idCliente=uuid4(),
        nombreCliente="Example Client",
        numeroCedula=28101010,
        emailCliente="prueba@example.com",
        numeroTelefono=584145556666
    )

    pedido = Pedido.create(
        idPedido=uuid4(),
        idCliente=cliente.idCliente.id,
        platillos=id_platillos,
        estadoPedido="CREADO",
        totalPedido=10.0
    )

    return pedido

