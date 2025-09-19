"PRUEBAS"
#----------------------------------#

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio)
print("EJERCICIO 8")

cantidad_numeros=int(input("Ingrese el número entero positivo límite: "))
while cantidad_numeros < 0:
    cantidad_numeros=int(input("Intente nuevamente: "))
contador_pares=0
contador_impares=0
contador_positivos=0
contador_negativos=0
for i in range(cantidad_numeros):
    num_ingresado=int(input(f"Ingrese el número {i+1} :"))
    if num_ingresado % 2 == 0:
        contador_pares +=1
    elif num_ingresado % 2 == 1:
        contador_impares +=1
    if num_ingresado > 0:
        contador_positivos +=1
    elif num_ingresado < 0:
        contador_negativos +=1

print(f"La cantidad de números pares es de: {contador_pares}")
print(f"La cantidad de números impares es de: {contador_impares}")
print(f"La cantidad de números positivos es de: {contador_positivos}")
print(f"La cantidad de números negativos es de: {contador_negativos}")
