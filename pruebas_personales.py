"PRUEBAS"
#----------------------------------#

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero_limite=int(input("Ingrese el número entero positivo límite: "))
suma=0
while numero_limite < 0:
    numero_limite=int(input("Intente nuevamente: "))
for i in range(numero_limite+1):
    suma=suma+i
print(suma)
