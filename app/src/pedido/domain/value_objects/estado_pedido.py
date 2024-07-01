from enum import Enum

class EstadoPedido(Enum):
    CREADO = 'CREADO'
    EN_PROCESO = 'EN_PROCESO'
    LISTO = 'LISTO'
    RECHAZADO = 'RECHAZADO'

    @staticmethod
    def create(estado: str) -> 'EstadoPedido':
        return EstadoPedido(estado)