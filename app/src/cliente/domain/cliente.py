from pydantic import BaseModel
from typing import List
from .value_objects.id_cliente import IdCliente

class Cliente:
    def __init__(self, _idCliente: IdCliente, _nombreCliente: NombreCliente, _numeroCedula: NumeroCedula, _emailCliente: EmailCliente, _numeroTelefono: NumeroTelefono): # type: ignore
        self._idCliente = _idCliente
        self._nombreCliente = _nombreCliente
        self._numeroCedula = _numeroCedula
        self._emailCliente = _emailCliente
        self._numeroTelefono = _numeroTelefono
    
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
    def create(cls, idCliente, nombreCliente, numeroCedula, emailCliente, numeroTelefono):
        return cls(
            idCliente=IdCliente.create(idCliente),
            nombreCliente=NombreCliente.create(nombreCliente), # type: ignore
            numeroCedula=NumeroCedula.create(numeroCedula), # type: ignore
            emailCliente=EmailCliente.create(emailCliente), # type: ignore
            numeroTelefono=NumeroTelefono.create(numeroTelefono) # type: ignore
        )