titulos=[]
ejemplares=[]
opciones=["1","2","3","4","5","6","7","8"]


cant_titulos_agregar=int(input("Ingrese la cantidad de títulos a agregar: "))
for i in range(cant_titulos_agregar):
    nuevo_titulo=input("Ingrese nuevo título: ").strip()
    titulos.append(nuevo_titulo)
    ejemplares.append(0)
    print(titulos)
    print(ejemplares)

for i in range(len(titulos)):
    print("La cantidad de ejemplares de ", titulos[i].title(), "es de ", ejemplares[i], ".")



#no prestar mas de lo disponible
#validar existencia de titulos en cada caso
