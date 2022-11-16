from typing import List
from .Parking_Lot import *

class Suv (ParkingLot):
    
    def _init_(self, NCarro:int, Nsuv:int, Nvan:int, tipo_Carro:str, cochesSuv:int, PagareSuv:int):
        """
         Clase constructor de Cars que hereda de la clase padre ParkinLot

        Args:
            NCarro (int): Introduces el número de plazas que hay dentro del parqueadero para los carros
            plazaSUV (int): Introduces el número de plazas que hay dentro del parqueadero disponibles para el SUV
            plazaVan (int): Introduces el número de plazas que hay dentro del parqueadero disponibles para la Van
            tipo_Carro (str): Introduces el tipo de carro que estas parqueando
            cochesSuv (int): introduces la cantidad de coches suv que entran
            PagareSuv (int): le asignas cuanto va a pagar por cada tiempo transcurrido
        """
        super()._init_(NCarro, Nsuv, Nvan, tipo_Carro)
        self.cochesSuv = cochesSuv
        self.PagareSuv = PagareSuv
        
    def Time(self):
       print("Puede ser parqueado a cualquier hora :)")
  
    def plazas(self):
        seleccion = "van"
      
        if self.tipo_Carro == seleccion:
            self.Nsuv = self.Nsuv - self.cochesSuv
            print("Los lugares que estan disponibles para el cohe tipo suv es:")
            print(self.Nsuv)
            
    def cobrohoras(self):
        horas= int(input("Inserte cuantas horas demoro su carro parqueado\t"))
        self.PagareSuv  = self.PagareSuv  * horas
        
        print(self.PagareSuv)
        
    def VerificacionDiaSiguiente():
        ...