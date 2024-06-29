from .value_objects.id_cliente import IdCliente
from .value_objects.nombre_cliente import NombreCliente
from .value_objects.cedula_cliente import NumeroCedula
from .value_objects.email_cliente import EmailCliente
from .value_objects.tlf_cliente import NumeroTelefono

class Cliente:
    def __init__(self, _idCliente: IdCliente, _nombreCliente: NombreCliente, _numeroCedula: NumeroCedula, _emailCliente: EmailCliente, _numeroTelefono: NumeroTelefono):
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
            nombreCliente=NombreCliente.create(nombreCliente),
            numeroCedula=NumeroCedula.create(numeroCedula),
            emailCliente=EmailCliente.create(emailCliente),
            numeroTelefono=NumeroTelefono.create(numeroTelefono)
        )