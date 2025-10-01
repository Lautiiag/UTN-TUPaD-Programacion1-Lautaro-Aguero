"Ahorcado temática de autos"
import random


def elegir_palabra(palabras):
    palabra_elegida=palabras[random.randrange(0,len(palabras))]
    return palabra_elegida


palabras=("auto","camioneta","moto","ford","chevrolet","camion","mustang","camaro","raptor","corvet")
palabra_elegida_afuera=elegir_palabra(palabras)
print(palabra_elegida_afuera)

print(len(palabra_elegida_afuera))


