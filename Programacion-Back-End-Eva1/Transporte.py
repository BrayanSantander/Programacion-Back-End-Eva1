class Transporte:
    def __init__(self,aro,peso) -> None:
        self.__COSTODESPACHOBASE = 4000
        self.__aro = aro
        self.__peso = peso
    
    def get_COSTODESPACHOBASE(self):
        return self.__COSTODESPACHOBASE
    
    def set_COSTODESPACHOBASE(self,COSTODESPACHOBASE):
        self.__COSTODESPACHOBASE = COSTODESPACHOBASE
    
    def get_aro(self):
        return self.__aro
    
    def set_aro(self,aro):
        self.__aro = aro
    
    def get_peso(self):
        return self.__peso
    
    def set_peso(self,peso):
        self.__peso = peso
    
    def calcularDespacho(self):
        return self.__COSTODESPACHOBASE
    
    def __str__(self):
        return f' Aro: {self.__aro} Peso: {self.__peso} Costo Despacho: {self.calcularDespacho()}'