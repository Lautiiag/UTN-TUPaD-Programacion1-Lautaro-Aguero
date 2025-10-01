"Ahorcado temática de vegetales y frutas"
import random


def elegir_palabra(palabras):
    palabra_elegida=palabras[random.randrange(0,len(palabras))]
    return palabra_elegida


palabras=("pera", "banana", "manzana", "naranja", "mandarina", "uva", "zapallo", "papa", "apio", "pepino", "durazno")
palabra_elegida_afuera=elegir_palabra(palabras)
print(palabra_elegida_afuera)

print(len(palabra_elegida_afuera))


