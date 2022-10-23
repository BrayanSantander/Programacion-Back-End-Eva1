from Tecnologia import Tecnologia
class Consola(Tecnologia):
    def __init__(self,voltaje,precio,eficiencia,marca,nombreConsola,version) -> None:
        super().__init__(voltaje,precio,eficiencia,marca)
        self.__nombreConsola = nombreConsola
        self.__version = version
    
    def get_nombreConsola(self):
        return self.__nombreConsola
    
    def set_nombreConsola(self,nombreConsola):
        self.__nombreConsola = nombreConsola
    
    def get_version(self):
        return self.__version
    
    def set_version(self,version):
        self.__version = version 
    
    def calcularDescuento(self):
        if self.__version == "Lite" or self.__version.lower() == "lite":
            descuento = self.__precio * 0.05
            descuentoTotal = super().calcularDescuento - descuento
            return descuentoTotal
        else:
            descuentoTotal = super().calcularDescuento
            return descuentoTotal
    
    def __str__(self):
         return f'{super().__str__()} Nombre la consola :{self.__nombreConsola} Version: {self.__version}'