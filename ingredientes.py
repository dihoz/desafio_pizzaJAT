def agregar_ingrediente(pizza):
    ingredientes=["tomate","champiñones","aceitunas","cebolla","pollo","jamon","carne","tocino","queso","piña"]
    ingredientesActuales= pizza["ingredientes"]
    IngredientesOpcion = [x for x in ingredientes if x not in ingredientesActuales]
    for x in range(len(IngredientesOpcion)):
        print(f" {x+1}.- {IngredientesOpcion[x]} ")
    ing = int(input("ingrese el ingrediente : "))
    pizza["ingredientes"].append(IngredientesOpcion[ing-1])

def quitar_ingrediente(pizza):
    #ingredientes=["tomate","champiñones","aceitunas","cebolla","pollo","jamon","carne","tocino","queso"]
    #ingredientesActuales= pizza["ingredientes"]
    IngredientesOpcion = [x for x in pizza["ingredientes"] ]
    for x in range(len(IngredientesOpcion)):
        print(f" {x+1}.- {IngredientesOpcion[x]} ")
    ing = int(input("ingrese el ingrediente : "))
    pizza["ingredientes"].pop(ing-1)