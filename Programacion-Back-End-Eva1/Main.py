from Bicicleta import Bicicleta
from Consola import Consola
from Scooter import Scooter
from TV import TV


listaTvs = []
listaConsolas = []
listaScooters = []
listaBicicletas = []

def menu():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("1.-Registrar Tv")
    print("2.-Registrar Consola")
    print("3.-Registrar Scooter")
    print("4.-Registrar Bicicleta")
    print("5.-Cotizar Tvs")
    print("6.-Cotizar Consolas")
    print("7.-Cotizar Scooters")
    print("8.-Cotizar Bicicletas")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    opcion = input("Ingrese una opción: ")
    if opcion =="1":
        registrarTv()
    elif opcion =="2":
        registrarConsolas()
    elif opcion =="3":
        registrarScooter()
    elif opcion =="4":
        registrarBicicleta()
    elif opcion =="5":
        cotizarTvs()
    elif opcion =="6":
        cotizarConsolas()
    elif opcion =="7":
        cotizarScooters()
    elif opcion =="8":
        cotizarBicicletas()
    else:
        print("Opción no valida")

def registrarTv():
    marca = input("Ingrese la marca de la Tv: ")
    voltaje = int(input("Ingrese el voltaje de la Tv: "))
    precio = float(input("Ingrese el precio de la Tv: "))
    eficiencia = input("Ingrese Eficiencia de la Tv (A-B-C-D-E-F): ")
    tamano = float(input("Ingrese tamaño de la Tv: "))
    tele = TV(voltaje,precio,eficiencia,marca,tamano)
    listaTvs.append(tele)

def registrarConsolas():
    nombre = input("Ingrese nombre de la consola: ")
    version = input("Ingrese version de la consola: ")
    marca = input("Ingrese la marca de la Consola: ")
    voltaje = int(input("Ingrese el voltaje de la Consola: "))
    precio = float(input("Ingrese el precio de la Consola: "))
    eficiencia = input("Ingrese Eficiencia de la Consola (A-B-C-D-E-F): ")
    consola = Consola(voltaje,precio,eficiencia,marca,nombre,version)
    listaConsolas.append(consola)

def registrarScooter():
    marca = input("Ingrese la marca del Scooter: ")
    voltaje = int(input("Ingrese el voltaje del Scooter: "))
    precio = float(input("Ingrese el precio del Scooter: "))
    eficiencia = input("Ingrese Eficiencia del Scooter (A-B-C-D-E-F): ")
    aro = float(input("Ingrese el aro del Scooter: "))
    velocidad = int(input("Ingrese la velocidad del Scooter: "))
    peso = float(input("Ingrese el peso del Scooter: "))
    scooter = Scooter(voltaje,precio,eficiencia,marca,aro,peso,velocidad)
    listaScooters.append(scooter)
    
def registrarBicicleta():
    aro = float(input("Ingrese el aro de la bicicleta: "))
    precio = float(input("Ingrese el precio de la bicicleta: "))
    peso = float(input("Ingrese el peso de la bicicleta: "))
    marca = input("Ingrese la marca de la bicicleta: ")
    bici = Bicicleta(aro,peso,precio,marca)
    listaBicicletas.append(bici)
    
def cotizarTvs():
    for teles in listaTvs:
        print(teles)

def cotizarConsolas():
    for consolas in listaConsolas:
        print(consolas)

def cotizarScooters():
    for scooter in listaScooters:
        print(scooter)

def cotizarBicicletas():
    for bici in listaBicicletas:
        print(bici)

while True:
    menu()