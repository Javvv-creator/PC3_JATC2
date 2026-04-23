# E8
# JATC
# Escribir un programa que lea la puntuación del usuario e indique su nivel
# de rendimiento, así como la cantidad de dinero que recibirá el usuario.

puntaje = float(input("introduzca su puntuacion: "))
inaceptable = 0
aceptable = 0.4
meritorio = 0.6

if puntaje == inaceptable:
    nivel = "Inaceptable"
elif puntaje == aceptable:
    nivel = "Aceptable"
else:
    nivel = "Meritorio"

print("el nivel de rendimiento es: ", nivel)
print("recibirá: ", (puntaje * 2400))