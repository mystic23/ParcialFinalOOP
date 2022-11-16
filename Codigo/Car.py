from typing import List
from .Parking_Lot import *

class Cars (ParkingLot):
    
    def _init_(self, NCarro:int, Nsuv:int, Nvan:int, tipo_Carro:str, cocheCar: int, pagareCar: int):
        """
        Clase constructor de Cars que hereda de la clase padre ParkinLot

        Args:
            NCarro (int): Introduces el número de plazas que hay dentro del parqueadero para los carros
            plazaSUV (int): Introduces el número de plazas que hay dentro del parqueadero disponibles para el SUV
            plazaVan (int): Introduces el número de plazas que hay dentro del parqueadero disponibles para la Van
            tipoCar (str): Introduces el tipo de carro que estas parqueando
            cocheCar (int): introduces la cantidad de carros compactos que hay
            pagareCar (int): Le asignas el valor que pagara por tanto tiempo transcurrido
        """
        super()._init_(NCarro, Nsuv, Nvan, tipo_Carro)
        self.cocheCar = cocheCar
        self.pagareCar = pagareCar
        
    def Time(self):
        print("Puede ser parqueado a cualquier hora :)")
  
    def plazas(self):
        C = "compacto"
        if self.tipo_Carro == C:
            self.NCarro = self.NCarro - self.cocheCar
            print(self.NCarro)  
    def cobrohoras(self):
        time= int(input("Inserte cuantas horas demoro su carro parqueado\t"))
        self.pagareCar = self.pagareCar * time
        print(self.pagareCar)
    def VerificacionDiaSiguiente():
        ...
