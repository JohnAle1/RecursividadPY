#Metodo para factorial
def factorial(n):
    if n == 1:  
        return 1
    else:  
        return n * factorial(n - 1)
#Metodo para total de paginas de libros
def totalPaginas(libros):
    if len(libros) == 1:
        return libros[0]
    else:
        return libros[0] + totalPaginas(libros[1:])
#Metodo de suma de un numero
def SumaRecursiva(n):
    if n==1:
        return 1
    else:
        return n + SumaRecursiva(n-1)
#Fibonaci recursivo
def fibonacci(n):
    # Caso base: si n es 0 o 1, devolver n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: sumar los dos valores anteriores
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
#Collatz Recursivo
def collatz(n):
    # Imprimir el número actual
    print(n, end=", ")
    # Caso base: si n es 1, terminar la recursión
    if n == 1:
        return
    # Caso recursivo: determinar si n es par o impar y llamar recursivamente
    elif n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)
# Potencia Recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
# Invertir Lista recursivo
def invertirLista(lista):
    if len(lista) <= 1:
        return lista
    else:
        return invertirLista(lista[1:]) + [lista[0]]
#Palindromo
def Palindromo(lista):
    if len(lista) <= 1:
        return True
    elif lista[0] == lista[-1]:
        return Palindromo(lista[1:-1])
    else:
        return False
#Maximo de una lista
def maximoLista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maximoNumero = maximoLista(lista[1:])
        return lista[0] if lista[0] > maximoNumero else maximoNumero

#MAIN PRINCIPAL
#print(fibonacci(11))
#print(factorial(3))
#print(totalPaginas([10,20,30,40]))
#print(SumaRecursiva(4))
#print(collatz(3))
#print(potencia(2,4))
#print(invertirLista(["J","o","h","n","n","y"]))
#print(Palindromo([1,2,3,2,1]))
print(maximoLista([1,10,2,0,-1]))