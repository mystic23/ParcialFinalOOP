from .Parking_Lot import *
class Usuario():
    
    @property
    def __init__(self, name: str, contraseña: str, registro: bool, cantidadUsuarios: int) -> None:
        self.name= name
        self.contraseña = contraseña
        self.registro = registro
        self.cantidadUsuarios = cantidadUsuarios
    
    def VerificarCuenta():
        ...
    
    def CrearCuenta():
        ...
    
    def EliminarCuenta():
        ...
        
    