from fastapi import APIRouter, Depends
from app.src.ingrediente.domain.value_objects.id_ingrediente import IdIngrediente
from app.src.ingrediente.domain.value_objects.cantidad_ingrediente import CantidadIngrediente
from app.src.ingrediente.domain.value_objects.nombre_ingrediente import NombreIngrediente
from app.src.ingrediente.domain.ingrediente import Ingrediente
from app.src.cliente.domain.cliente import Cliente
from app.src.almacen.domain.almacen import Almacen
from app.src.common.infrastructure.modelos_pydantic import *
from app.src.platillo.domain.platillo import Platillo
from app.src.pedido.domain.pedido import Pedido
from app.src.common.infrastructure.auth import user_dependency
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

@router.get("/ingredientes/", response_model=IngredienteModel)
@as_pydantic_model
async def get_ingredient(token: str = Depends(oauth2_scheme)):
    # Create a new Ingrediente every time this function is called
    ingrediente = Ingrediente.create(
        nombreIngrediente="Example Ingredient",
        cantidadIngrediente=100
    )
    return ingrediente#.to_model()

@router.get("/almacen/", response_model=AlmacenModel)
@as_pydantic_model
async def get_almacen(token: str = Depends(oauth2_scheme)):
    # Create a new Almacen
    almacen = Almacen.create(capacidadMaxima=1000.0)

    # Create a few Ingredientes and add them to the Almacen
    for _ in range(3):
        ingrediente = Ingrediente.create(
            nombreIngrediente="Example Ingredient",
            cantidadIngrediente=100.0
        )
        almacen.agregarIngrediente(ingrediente.idIngrediente)

    return almacen

@router.get("/clientes/", response_model=ClienteModel)
@as_pydantic_model
async def get_client(token: str = Depends(oauth2_scheme)):
    # Create a new Cliente
    cliente = Cliente.create(
        nombreCliente="Example Client",
        numeroCedula=28101010,
        emailCliente="prueba@example.com",
        numeroTelefono=584145556666
    )
    return cliente

@router.get("/platillos/", response_model=PlatilloModel)
@as_pydantic_model
async def get_platillo(token: str = Depends(oauth2_scheme)):

    ingredientes = []
    for _ in range(3):
        ingrediente = Ingrediente.create(
            nombreIngrediente="Example Ingredient",
            cantidadIngrediente=100.0
        )
        ingredientes.append(ingrediente)

    id_ingredientes = [ingrediente.idIngrediente for ingrediente in ingredientes]

    platillo = Platillo.create(
        nombrePlatillo="Example Platillo",
        precioPlatillo=10.0,
        descripcionPlatillo="This is an example platillo",
        tipoPlatillo="PIZZA",
        ingredientesPlatillo=id_ingredientes
    )

    return platillo

@router.get("/pedidos/", response_model=PedidoModel)
@as_pydantic_model
async def get_pedido(token: str = Depends(oauth2_scheme)):

    ingredientes = []
    for _ in range(3):
        ingrediente = Ingrediente.create(
            nombreIngrediente="Example Ingredient",
            cantidadIngrediente=100.0
        )
        ingredientes.append(ingrediente)

    platillos = [Platillo.create(
        nombrePlatillo="Example Platillo",
        precioPlatillo=10.0,
        descripcionPlatillo="This is an example platillo",
        tipoPlatillo="PIZZA",
        ingredientesPlatillo=ingredientes
    )]

    id_platillos = [platillo.idPlatillo for platillo in platillos]

    cliente = Cliente.create(
        nombreCliente="Example Client",
        numeroCedula=28101010,
        emailCliente="prueba@example.com",
        numeroTelefono=584145556666
    )

    pedido = Pedido.create(
        idCliente=cliente.idCliente,
        platillos=id_platillos,
        totalPedido=10.0
    )

    return pedido

