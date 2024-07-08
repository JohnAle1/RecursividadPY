#Fibonaci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Invertir Lista recursivo
def invertirLista(lista):
    if len(lista) <= 1:
        return lista
    else:
        return invertirLista(lista[1:]) + [lista[0]]

#Palindromo
def Palindromo(lista):
    if len(lista) <= 1:
        return "Es palindorme"
    elif lista[0] == lista[-1]:
        return Palindromo(lista[1:-1])
    else:
        return "No es palindroma"
    
#print(fibonacci(5))
#print(invertirLista(["J","o","h","n","n","y"]))
#print(Palindromo([1,2,3,2,1]))