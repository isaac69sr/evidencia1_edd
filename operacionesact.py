import datetime
from math import trunc
from random import randint, random
from datetime import date
from os import system

from datetime import datetime

now = datetime.now()

hoy = now.strftime("%m/%d/%Y")


#diccionario = {5:["refacciones","descripciones","precio","s","i"]}

diccionario = {}
def fecha_folio(r,d,c,s,i):
  a = randint(0,9)
  b = randint(0,9)
  j = randint(0,9)
  x = (a*100) + (b * 10) + j
  while diccionario.__contains__(x):
   print("creando")
   system('cls')
        
  else:
    diccionario[x] = [r,d,c,hoy,s,i]
    print("Folio: ",x," Fecha: ", hoy, "\nCantidad de articulos: ", r.__len__(), "\nCompra total de: $", s, 
    "\nIva correspondiente: $", i, "\nTotal a pagar: $",s+i,"\nPrecione tecla \"enter\" para continuar")

class operaciones:
    def agregar_venta():

      suma = 0
      continuar = 0
      while continuar != "2":
        system('cls')
        print("Venta\n************************************\n")
        Art = input("Articulo de Venta: ")
        Desc = input("Redacte una breve descripción: ")
        prec = input("adjente el precio (sin signo de denominación ): ")
        if suma == 0:
          refacciones = [Art]
          descripciones = [Desc]
          precio = [prec]
        else:
          refacciones[len(refacciones):] = [Art]
          descripciones[len(descripciones):] = [Desc] 
          precio[len(precio):] = [prec]
        suma = suma + int(prec)
        iva = suma*.16
        continuar = input("¿Desea agregar un nuevo articulo? 1.- agregar articulo 2.- Para finalizar venta.\nSelección: ")
        system('cls')
      fecha_folio(refacciones,descripciones,precio,suma,iva)

    def mostrar_venta():
      conteo = 1
      system('cls')
      print("Registro de Venta por Código\n************************************\n")
      for key in diccionario.keys() :
        print (conteo,"-: ", key)
        conteo += 1
    def detalle_venta(f):
      system('cls')
      f = int(f)
      print("Información detallada\n************************************\n")
      if diccionario.__contains__(f):
        print("Venta con código: ", f," Registrada el: ",diccionario[f].__getitem__(3),"\nPrecio Total: ",diccionario[f].__getitem__(4), "\nIva de la Venta: ",diccionario[f].__getitem__(5),"\n**************************")
        print("Cantidad de articulos Vendidos: ", diccionario[f].__getitem__(0).__len__())
        item = 0
        ##for item in diccionario[f].__getitem__(0).__len__():
          ##print ("1.- ", diccionario[f].__getitem__(0)[item])
        while item < diccionario[f].__getitem__(0).__len__() :  
          print (item+1,".- \nArticulo: ", diccionario[f].__getitem__(0)[item], "\nDescripción: ",diccionario[f].__getitem__(1)[item],"\nPrecio Unitario: ", diccionario[f].__getitem__(2)[item])
          # Increment the value of the variable "number by 1"
          item = item+1
        print("\nPrecione tecla \"enter\" para continuar")
      else:
        print("Código de Venta no encontrado\n Presione \"enter\" para continuar")




    


      
        


