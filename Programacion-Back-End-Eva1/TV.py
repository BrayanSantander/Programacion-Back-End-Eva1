from Tecnologia import Tecnologia
class TV(Tecnologia):
    def __init__(self,voltaje,precio,eficiencia,marca,tamano) -> None:
        super().__init__(voltaje,precio,eficiencia,marca)
        self.__tamano = tamano
    
    def get_tamano(self):
        return self.__tamano
    
    def set_tamano(self,tamano):
        self.__tamano = tamano
    
    def __str__(self):
        return f'{super().__str__()} Tamaño: {self.__tamano}'
       
    