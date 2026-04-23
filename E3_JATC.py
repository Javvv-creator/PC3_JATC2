#E3
#JATC
#Escribir un programa que pida al usuario dos números y muestre por
#pantalla su división. Si el divisor es cero el programa debe mostrar un
#error.

n1 = int(input("ingrese el numero 1: "))
n2 = int(input("ingrese el numero 2: "))

if n2 == 0:
    print("no se puede dividir por 0.")
else:
    print("resultado: ", n1/n2)
