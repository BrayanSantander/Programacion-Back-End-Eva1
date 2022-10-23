class Tecnologia:
    def __init__(self,voltaje,precio,eficiencia,marca) -> None:
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca
    
    def get_voltaje(self):
        return self.__voltaje
    
    def set_voltaje(self,voltaje):
        self.__voltaje = voltaje
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio = precio
    
    def get_eficiencia(self):
        return self.__eficiencia
    
    def set_eficiencia(self,eficiencia):
        self.__eficiencia = eficiencia
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self,marca):
        self.__marca = marca
    
    def calcularDescuento(self):
        if self.__eficiencia=='A' or self.__eficiencia=='B' or self.__eficiencia=='a' or self.__eficiencia=='b':
            descuento = self.__precio * 0.5
            total = self.__precio-descuento
            return descuento
        elif self.__eficiencia=='C' or self.__eficiencia=='D' or self.__eficiencia=='c' or self.__eficiencia=='d':
            descuento = self.__precio * 0.3
            total = self.__precio-descuento
            return descuento
        elif self.__eficiencia=='E' or self.__eficiencia=='F' or self.__eficiencia=='e' or self.__eficiencia=='f':
            descuento = self.__precio * 0.1
            total = self.__precio-descuento
            return descuento
        else:
            return 0
        
    def __str__(self):
        return f'*Voltaje:{self.__voltaje}v *Precio: ${self.__precio} *Eficiencia: {self.__eficiencia} *Marca: {self.__marca} *Descuento: ${self.calcularDescuento()}'