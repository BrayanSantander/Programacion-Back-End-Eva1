from Tecnologia import Tecnologia
from Transporte import Transporte
class Scooter(Tecnologia,Transporte):
    def __init__(self,voltaje,precio,eficiencia,marca,aro,peso,velocidad) -> None:
        super().__init__(voltaje,precio,eficiencia,marca)
        super().__init__(aro,peso)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
           
    def get_velocidad(self):
        return self.__velocidad
    
    def set_velocidad(self,velocidad):
        self.__velocidad = velocidad
    
    def calcularDespacho(self):
        preciokilo = self.__peso * 300
        despachoTotal = super().calcularDespacho()+preciokilo
        return despachoTotal

    def __str__(self):
        return f'{super().__str__()} Velocidad: {self.__velocidad} Eficiencia: {self.__eficiencia} Voltaje: {self.__voltaje} Precio: {self.__precio} marca: {self.__marca}'