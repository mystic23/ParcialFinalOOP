from typing import List
from Parking_Lot import *

class Van (ParkingLot):
    def _init_(self, NCarro:int, Nsuv:int, Nvan:int, tipo_Carro:str, cochesVan: int, pagareVan: int):
        """
        Clase constructor de Van que hereda de la clase padre ParkinLot


        Args:
           NCarro (int): Introduces el número de plazas que hay dentro del parqueadero para los carros
            plazaSUV (int): Introduces el número de plazas que hay dentro del parqueadero disponibles para el SUV
            plazaVan (int): Introduces el número de plazas que hay dentro del parqueadero disponibles para la Van
            tipo_Carro (str): Introduces el tipo de carro que estas parqueando
            cochesVan (int): introduces la cantidad de coches van que entran
            PagareVan (int): le asignas cuanto va a pagar por cada tiempo transcurrido por la van
        """
        
        super()._init_(NCarro, Nsuv, Nvan, tipo_Carro)
        
        self.cochesVan = cochesVan
        self.pagareVan = pagareVan
        
    def Time(self):
        print("Puede ser parqueado a cualquier hora :)")
        
    def plazas(self):
        V = "van"
        if self.tipoCars == V:
            self.Nvan = self.Nvan - self.cochesVan
            print(self.Nvan)
            
    def cobrohoras(self):
        horas= int(input("Inserte cuantas horas demoro su carro parqueado\t"))
        self.pagareVan  = self.pagareVan  * horas
        print(self.pagareVan)
    
    def VerificacionDiaSiguiente():
        ...
    
