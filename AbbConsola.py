class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

# Ejemplo de uso:
arbol = ArbolBinario()
nodos = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for valor in nodos:
    arbol.insertar(valor)

# Buscar un nodo específico, por ejemplo el nodo con valor 6
nodo_buscado = arbol.buscar(6)
if nodo_buscado:
    print(f"Se encontró el nodo con valor {nodo_buscado.valor}")
else:
    print("No se encontró el nodo.")

# Buscar un nodo que no existe, por ejemplo el nodo con valor 15
nodo_no_encontrado = arbol.buscar(15)
if nodo_no_encontrado:
    print(f"Se encontró el nodo con valor {nodo_no_encontrado.valor}")
else:
    print("No se encontró el nodo.")
