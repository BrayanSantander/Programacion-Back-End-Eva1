from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self,aro,peso,precio,marca) -> None:
        super().__init__(aro,peso)
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca
           
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio = precio
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self,marca):
        self.__marca = marca
    
    def calcularDespacho(self):
        preciokilo = self.__peso * 400
        despachoTotal = super().calcularDespacho()+preciokilo
        return despachoTotal
    
    def __str__(self):
         return f'{super().__str__()} Precio: {self.__precio} marca: {self.__marca}'