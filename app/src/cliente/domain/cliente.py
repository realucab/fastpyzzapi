from typing import List
from .value_objects.id_cliente import IdCliente
from .value_objects.nombre_cliente import NombreCliente
from .value_objects.numero_cedula import NumeroCedula
from .value_objects.email_cliente import EmailCliente
from .value_objects.numero_telefono import NumeroTelefono
from uuid import uuid4
class Cliente:
    
    def __init__(self, idCliente: IdCliente, nombreCliente: NombreCliente, numeroCedula: NumeroCedula, emailCliente: EmailCliente, numeroTelefono: NumeroTelefono):
        self._idCliente = idCliente
        self._nombreCliente = nombreCliente
        self._numeroCedula = numeroCedula
        self._emailCliente = emailCliente
        self._numeroTelefono = numeroTelefono
    
    @property
    def idCliente(self):
        return self._idCliente
    
    @property
    def nombreCliente(self):
        return self._nombreCliente
    
    @property
    def numeroCedula(self):
        return self._numeroCedula
    
    @property
    def emailCliente(self):
        return self._emailCliente
    
    @property
    def numeroTelefono(self):
        return self._numeroTelefono
    
    @classmethod
    def create(cls, nombreCliente: str, numeroCedula: int, emailCliente: str, numeroTelefono: int):
        return cls(
            idCliente=uuid4(),
            nombreCliente=NombreCliente.create(nombreCliente),
            numeroCedula=NumeroCedula.create(numeroCedula),
            emailCliente=EmailCliente.create(emailCliente),
            numeroTelefono=NumeroTelefono.create(numeroTelefono)
        )
    
    def to_dict(self):
        return {
            'idCliente': str(self._idCliente),
            'nombreCliente': self._nombreCliente.nombre,
            'numeroCedula': self._numeroCedula.cedula,
            'emailCliente': self._emailCliente.email,
            'numeroTelefono': self._numeroTelefono.tlf
        }