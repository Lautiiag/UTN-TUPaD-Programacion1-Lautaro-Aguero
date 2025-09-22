"CASO 2 PARCIAL 1: CLINICA"

# Inicialización de listas y variables
especialidades=[]
cupos=[]

# Menú
print("MENÚ CLÍNICA")
print("1. Ingresar lista de especialidades")
print("2. Ingresar lista de cupos disponibles por especialidad")
print("3. Mostrar agenda")
print("4. Consultar cupos de una especialidad")
print("5. Listar especialidades sin cupo")
print("6. Ver sin cupo")
print("7. Actualizar cupos (reservar/cancelar): ")
print("8. Ver agenda: ")
print("9. Salir")

# Elegir opción
opciones=["1","2","3","4","5","6","7","8","9"]

salir=False
while salir == False:

    opcion=(input("Ingrese una opción: ")) 
    while opcion not in opciones:
        opcion=(input("Ingrese una opción válida: "))

    match opcion:
        case "1":
            
            print("Ingreso 1")
        case "2":
            print("Ingreso 2")
        case "3":
            print("Ingreso 3")
        case "4":
            print("Ingreso 4")
        case "5":
            print("Ingreso 5")
        case "6":
            print("Ingreso 6")
        case "7":
            print("Ingreso 7")
        case "8":
            print("Ingreso 8")
        case "9":
            salir=True
