"AUXILIAR"
#----------------------------------#

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
# Diccionario de productos con su stock
print("Ejercicio 8")
productos = {
    "leche": 10,
    "pan": 25,
    "arroz": 15,
}

# Mostrar productos disponibles
print("Productos disponibles actualmente:")
for nombre, stock in productos.items():
    print(f"- {nombre}: {stock} unidades")

# Solicitar producto al usuario
producto = input("Ingrese el nombre del producto que desea consultar: ").lower()

# Verificar si el producto existe en el diccionario
if producto in productos:
    print(f"El producto '{producto}' tiene {productos[producto]} unidades en stock.")

    # Consultar si desea agregar más unidades
    opcion = input("¿Desea agregar unidades a este producto? (s/n): ").lower()
    if opcion == "s":
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        productos[producto] += cantidad
        print(f"Se agregaron {cantidad} unidades. Nuevo stock de '{producto}': {productos[producto]} unidades.")
    else:
        print("No se modificó el stock.")

else:
    print(f"El producto '{producto}' no existe en el inventario.")
    opcion = input("¿Desea agregarlo al diccionario? (s/n): ").lower()
    if opcion == "s":
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        productos[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
    else:
        print("No se agregó el producto.")

# Mostrar diccionario actualizado
print("Stock actualizado de productos:")
for nombre, stock in productos.items():
    print(f"- {nombre}: {stock} unidades")
