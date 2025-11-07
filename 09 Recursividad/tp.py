"Tp Recursividad"
# Ejercicio 1: Factorial

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def calcular_factoriales():
    try:
        numero_maximo = int(input())
    except ValueError:
        return

    for i in range(1, numero_maximo + 1):
        print(f"El factorial de {i} es: {factorial_recursivo(i)}")

# Ejercicio 2: Serie de Fibonacci

def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def mostrar_serie_fibonacci():
    try:
        posicion_maxima = int(input())
    except ValueError:
        return

    serie = []
    for i in range(posicion_maxima + 1):
        serie.append(fibonacci_recursivo(i))
    
    print(serie)

# Ejercicio 3: Potencia

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1 / potencia_recursiva(base, -exponente)
    return base * potencia_recursiva(base, exponente - 1)

def probar_potencia():
    base = 2
    exponente = 10
    resultado = potencia_recursiva(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")

# Ejercicio 4: Decimal a Binario

def decimal_a_binario_recursivo(decimal):
    if decimal == 0:
        return "0"
    if decimal == 1:
        return "1"
    
    cociente = decimal // 2
    resto = decimal % 2
    
    return decimal_a_binario_recursivo(cociente) + str(resto)

# Ejercicio 5: Palíndromo

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])

# Ejercicio 6: Suma de Dígitos

def suma_digitos(n):
    if n == 0:
        return 0
    
    ultimo_digito = n % 10
    resto_numero = n // 10
    
    return ultimo_digito + suma_digitos(resto_numero)

# Ejercicio 7: Contar Bloques de Pirámide

def contar_bloques(n):
    if n <= 0:
        return 0
    
    # El total es la suma de los bloques del nivel actual (n) más
    # la suma de los bloques de los niveles superiores (contar_bloques(n-1))
    return n + contar_bloques(n - 1)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    
    contador = 0
    if ultimo_digito == digito:
        contador = 1
        
    return contador + contar_digito(resto_numero, digito)
