# E6
# JATC
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nom
# bre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres
# con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pre
# gunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("ingrese su nombre: ")
genero = input("ingrese su genero: ")

if (nombre.lower() < "m" and genero == "M") or (nombre.lower() > "n" and genero == "H"):
    print("su grupo es A") 
else:
    print("su grupo es B")