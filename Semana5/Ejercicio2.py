'''Control de temperatura
Un sistema de climatización clasifica:
"Fría": menos de 10°C
"Templada": entre 10 y 25
"Calurosa": más de 25
Solicita la temperatura e indica la clasificación correspondiente.
'''

x = int(input("Ingresa la temperatura para clasificarla:"))
if x<=10 :
    print("La temperatura es fria")
elif 10<x<=25:
    print("La temperatura es templada")
elif x>=26:
    print("La temperatura es caluorsa")




