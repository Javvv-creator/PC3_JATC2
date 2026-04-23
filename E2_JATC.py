#E2
#JATC
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al
#usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la
#guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

dato = "contraseña"

dato1 = input("ingrese la contraseña: ")

if dato == dato1.lower():
    print("la contraseña coincide")
else:
    print("la contraseña no coincide")