"AUXILIAR"
#----------------------------------#

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.
print("Ejercicio 8")

def calcular_imc(peso, altura):
    print(f"Su Índice de Masa Corporal es de: {round((peso/(altura**2)), 2)}")

peso_usuario=float(input("Ingrese su peso en kilogramos: "))
altura_usuario=float(input("Ingrese su altura en metros: "))
calcular_imc(peso_usuario, altura_usuario)
