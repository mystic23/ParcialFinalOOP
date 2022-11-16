from typing import List
from abc import ABC, abstractmethod
from .usuario import Usuario
from .Car import Cars
from .Van import Van
from .suv import Suv

class ParkingLot(ABC):
    
    @abstractmethod
    def _init_(self,Cantidad:int, NCarro:int, Nsuv:int, Nvan:int, tipo_Carro:str) -> None:
        """
          Clase constructor de Parqueadero
        Args:
            Cantidad(int): Numero lugares disponibles en el parqueadero
            NCarro (int): Introduces el número de plazas que hay dentro del parqueadero para los carros
            plazaSUV (int): Introduces el número de plazas que hay dentro del parqueadero disponibles para el SUV
            plazaVan (int): Introduces el número de plazas que hay dentro del parqueadero disponibles para la Van
            tipo_Carro (str): Introduces el tipo de carro que estas parqueando
        """
        self.Cantidad = Cantidad
        self.NCarro = NCarro
        self.Nsuv = Nsuv
        self.Nvan = Nvan
        self.tipo_Carro = tipo_Carro
    
    @abstractmethod
    def plazas(self):
        pass
        
    @abstractmethod
    def Time(self):
        pass
    
    @abstractmethod
    def cobrohoras(self):
        pass
 
class Verificacion(ParkingLot):
    
    @property
    def lugar(self)->bool:
        """
        property decoraator para verificar si hay plazas o no 
        """
        if self.Cantidad == 0:
            return False
        else:
            return True


    
        
    
        

