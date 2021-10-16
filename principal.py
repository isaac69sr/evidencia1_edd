from os import system
from operacionesact import operaciones, diccionario
##importación de librerias, y librerias personalizada
folio = 0
datos = ["1","2","3"]
seleccion = 1
##Menu
while seleccion != "3":
    system('cls')
    print("Menu\n1.- Registrar Venta\n2.- Consultar Venta.\n3.- Salir\nOpción Seleccionada: ")
    if seleccion == "1":

        operaciones.agregar_venta()
        ##CICLO MENU
    if seleccion == "2":
        if diccionario.__len__() == 0: 
            print("sin datos.")
        else:
            print("Ventas Relaizadas(código)\n")
            operaciones.mostrar_venta() ##uso de clase
            print("Para ver detallada la información esriba el código de la venta:\n Su selección: ")
            x = input()
            operaciones.detalle_venta(x)
    if seleccion == "3":
     print("Buen Día")
    seleccion = input()
print("Buen Día")
    




##print(diccionario[0].__getitem__(1)[0]) ## asi seleccionamos en un diccionario un elemento dentro de una lista que esta dentro de un diccionario