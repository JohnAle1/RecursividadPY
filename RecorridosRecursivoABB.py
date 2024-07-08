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

    def en_orden(self, nodo):
        if nodo:
            self.en_orden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.en_orden(nodo.derecha)

    def pre_orden(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.pre_orden(nodo.izquierda)
            self.pre_orden(nodo.derecha)

    def post_orden(self, nodo):
        if nodo:
            self.post_orden(nodo.izquierda)
            self.post_orden(nodo.derecha)
            print(nodo.valor, end=' ')

# Crear el árbol binario complejo
arbol = ArbolBinario()
nodos = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for valor in nodos:
    arbol.insertar(valor)

# Realizar los recorridos
print("Recorrido en Orden:")
arbol.en_orden(arbol.raiz)
print("\nRecorrido en Preorden:")
arbol.pre_orden(arbol.raiz)
print("\nRecorrido en Postorden:")
arbol.post_orden(arbol.raiz)
