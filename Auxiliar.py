"AUXILIAR"
#----------------------------------#

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_precio_final(precio, descuento=0):
    precio_final = precio - (precio * descuento / 100)
    return round(precio_final, 2)

resultado = calcular_precio_final(120, 15)
print(resultado)

num={1,2,3}
print(num)
