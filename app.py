from menu import menu
from masas_salsas import cambiar_masa,cambiar_salsa
from ingredientes import agregar_ingrediente, quitar_ingrediente
from tiempo import tiempopizza
import os
os.system('cls')
#menu interactivo
#permita cambiar el tipo de masa
#seleccionar tipo de salsa
#permita modificar ingredientes (agregar y Eliminar)
#opcion que permita mirar los ingredientes 
pizza = {"masa":"Tradicional","salsa":"tomate","ingredientes":["queso"]}
#pizza["ingredientes"].append("champiñones")
#pizza["salsa"]="pesto"
#pizza["ingredientes"].pop(pizza["ingredientes"].index("queso"))
while True: 
    os.system("cls")
    menu()
    print(pizza)

    valor = int(input("ingrese opción : "))
    if valor==1:
        tipomasa=cambiar_masa()
        if tipomasa == 1:
            pizza["masa"]="Masa delgada" 
        elif tipomasa == 2:
            pizza["masa"]="Masa borde queso" 
        elif tipomasa == 3:
            pizza["masa"]="Masa tradicional" 
    if valor==2:
        tiposalsa=cambiar_salsa()
        if tiposalsa == 1:
            pizza["salsa"]="alfredo" 
        elif tiposalsa == 2:
            pizza["salsa"]="pesto" 
        elif tiposalsa == 3:
            pizza["salsa"]="barbecue" 
        elif tiposalsa == 4:
            pizza["salsa"]="tomate"    
    elif valor==3:
        agregar_ingrediente(pizza)
    elif valor==4:
        quitar_ingrediente(pizza)
    elif valor==5:
        print(pizza)
    elif valor==6:
        os.system("cls")
        listaingredientes = ", "
        print(f"\nsu pizza estará lista en {tiempopizza(pizza)} minutos")
        print("su pizza es con :")
        print(f"masa : {pizza["masa"]}")
        print(f"salsa : {pizza["salsa"]}")
        print(f"ingredientes : {listaingredientes.join(pizza['ingredientes'])}")
        break
    elif valor==7:
        break

#main
#módulo menu    
#módulo masa y salsas
#módulo ingredientes
#módulo tiempo