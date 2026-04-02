'''Cajero automático: validación de retiro
Un cajero permite retirar solo montos mayores a 0 y múltiplos de 10.
Solicita el monto hasta que sea válido y luego muestra "Retiro exitoso".'''

print("Cajero automatico")
entrar = 0
input("Ingresa 0 para entrar")
while entrar == 0:
    a = int(input("Ingrese un monto para retirar:"))
    if (0 < a) and (a % 10 == 0) : 
        print ("Retiro exitoso")
    else :
        print ("Ingrese un monto valido")   
