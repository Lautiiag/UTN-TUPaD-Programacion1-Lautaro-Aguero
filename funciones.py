"FUNCIONES PERSONALIZADAS LAUTARO AGUSTÍN AGÜERO"

def armado_de_lista_con_ingreso_usuario(a): # a=espacios a agregar ingresador por usuario
    
    lista=()
    for elementos_agregados in range(0,a):
        lista.append(0)
    return lista

cantidad_espacios=int(input("Cantidad de espacios: "))


def ingreso_int(int_ingresado):
    dato_ingresado_correcto=False
    while dato_ingresado_correcto == False:
        try:
            int_ingresado=int(input("Ingrese la cantidad de espacios: "))
            dato_ingresado_correcto=True
        except:
            print("No ingresó un número válido.")
    return int_ingresado
