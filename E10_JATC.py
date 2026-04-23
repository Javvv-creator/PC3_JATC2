# E10
# JATC
# Escribir un programa que pregunte al usuario si quiere una pizza vegeta
# riana o no, y en función de su respuesta le muestre un menú con los in
# gredientes disponibles para que elija. Solo se puede eligir un ingre
# diente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o
# no y todos los ingredientes que lleva.

pizza = int(input("Bienvenido, Menu:\n 1. Pizza vegetariana. \n 2. Pizza no vegetariana \nseleccione una opcion: "))

if pizza == 1:
    print("ingredientes de pizzas vegetarianas: ")
    print("1. Pimiento")
    print("2. tofu")
    ingrediente = int(input("cual desea poner? "))
    if ingrediente == 1:
        ingrediente= "Pimiento"
    else:
        ingrediente = "tofu"
else:
    print("ingredientes de pizzas no vegetarianas: ")
    print("1. peperoni\n2. Jamon\n3. Salmon")
    ingrediente = int(input("cual desea poner? "))
    if ingrediente == 1:
        ingrediente = "Peperoni"
    elif ingrediente == 2:
        ingrediente = "Jamon"
    elif ingrediente == 3:
        ingrediente = "Salmon"
    else: 
        print("error!.")

print("Pizza vegetariana con mozzarella, tomate y", ingrediente)