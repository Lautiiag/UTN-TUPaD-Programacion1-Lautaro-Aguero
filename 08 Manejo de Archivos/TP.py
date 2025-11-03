"Tp Manejo de archivos"
#Funciones
#1
def crear_archivo_inicial():
    productos_iniciales = [
        "Mouse Gamer,25.99,10",
        "Teclado Mecánico,75.50,5",
        "Monitor LED 27,250.00,3"
    ]
    try:
        with open("productos.txt", "w") as archivo:
            for producto in productos_iniciales:
                archivo.write(producto + "\n")
        print("✅ Archivo 'productos.txt' creado exitosamente con 3 productos iniciales.")
    except IOError as e:
        print(f"Error al crear el archivo: {e}")
#2
def leer_y_mostrar_productos():
    print("\n--- Listado de Productos (Consigna 2) ---")
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                datos = linea_limpia.split(",")
                if len(datos) == 3:
                    nombre, precio, cantidad = datos
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
                else:
                    print(f"⚠️ Línea con formato incorrecto: {linea_limpia}")
                    
    except FileNotFoundError:
        print("Error: El archivo 'productos.txt' no se encontró. Ejecuta primero la Consigna 1.")
    except IOError as e:
        print(f"Error de lectura del archivo: {e}")
#3
def agregar_producto_desde_teclado():
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del nuevo producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Precio debe ser un número y Cantidad un entero.")
    nueva_linea = f"{nombre},{precio:.2f},{cantidad}\n"
    try:
        with open("productos.txt", "a") as archivo:
            archivo.write(nueva_linea)
        print(f"✅ Producto '{nombre}' agregado exitosamente al archivo.")
    except IOError as e:
        print(f"❌ Error al escribir en el archivo: {e}")
#4
def cargar_productos_a_lista():
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                datos = linea_limpia.split(",")
                
                if len(datos) == 3:
                    producto = {
                        "nombre": datos[0],
                        "precio": float(datos[1]),
                        "cantidad": int(datos[2])
                    }
                    productos.append(producto)
    
    except FileNotFoundError:
        print("Error: El archivo 'productos.txt' no se encontró.")
    except ValueError:
        print("Error de formato en los datos (precio o cantidad no son números válidos).")
    except IOError as e:
        print(f"Error de lectura: {e}")
        
    return productos
#5
def buscar_producto_por_nombre(productos):
    print("\n--- Buscar Producto ---")
    if not productos:
        print("La lista de productos está vacía.")
        return

    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    encontrado = False
    
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print("\n¡Producto encontrado! Datos:")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']:.2f}")
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"Error: El producto '{nombre_buscado}' no se encontró en la lista.")
#6
def guardar_productos_actualizados(productos):
    print("\n--- Guardar Productos Actualizados ---")
    try:
        with open("productos.txt", "w") as archivo:
            for producto in productos:
                linea = f"{producto['nombre']},{producto['precio']:.2f},{producto['cantidad']}\n"
                archivo.write(linea)
        
        print("Archivo 'productos.txt' sobrescrito exitosamente con los datos actualizados.")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")


#Main
#1
crear_archivo_inicial()
#2
leer_y_mostrar_productos()
#3
agregar_producto_desde_teclado()
leer_y_mostrar_productos() # Mostrar para verificar que se agregó el producto
#4
lista_productos_memoria = cargar_productos_a_lista()
print("\n--- Lista de Diccionarios en Memoria (Consigna 4) ---")
print(lista_productos_memoria)
#5
buscar_producto_por_nombre(lista_productos_memoria)
#6
guardar_productos_actualizados(lista_productos_memoria)
