import tkinter as tk

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

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Arbol Binario")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.label = tk.Label(self.frame, text="Ingrese un valor: ")
        self.label.pack(side=tk.LEFT, padx=10)
        
        self.entry = tk.Entry(self.frame)
        self.entry.pack(side=tk.LEFT, padx=10)
        
        self.button = tk.Button(self.frame, text="Agregar Nodo", command=self.insertar_valor)
        self.button.pack(side=tk.LEFT, padx=10)
        
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()
        
        self.arbol = ArbolBinario()

    def insertar_valor(self):
        try:
            valor = int(self.entry.get())
            self.arbol.insertar(valor)
            self.entry.delete(0, tk.END)
            self.dibujar_arbol()
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    def dibujar_arbol(self):
        self.canvas.delete("all")
        if self.arbol.raiz is not None:
            self._dibujar_nodo(self.arbol.raiz, 400, 50, 100)

    def _dibujar_nodo(self, nodo, x, y, espacio):
        if nodo.izquierda is not None:
            self.canvas.create_line(x, y, x - espacio, y + 50)
            self._dibujar_nodo(nodo.izquierda, x - espacio, y + 50, espacio / 2)
        if nodo.derecha is not None:
            self.canvas.create_line(x, y, x + espacio, y + 50)
            self._dibujar_nodo(nodo.derecha, x + espacio, y + 50, espacio / 2)
        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="pink")
        self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 12))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()