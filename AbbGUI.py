import tkinter as tk
from tkinter import messagebox

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

class BSTApp:
    def __init__(self, root):
        self.root = root
        self.tree = None

        self.root.title("Árbol Binario de Búsqueda")

        self.label = tk.Label(root, text="Ingrese un valor:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.insert_button = tk.Button(root, text="Insertar", command=self.insert_value)
        self.insert_button.pack()

        self.search_button = tk.Button(root, text="Buscar", command=self.search_value)
        self.search_button.pack()

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

    def insert_value(self):
        value = self.entry.get()
        if value.isdigit():
            self.tree = insert(self.tree, int(value))
            messagebox.showinfo("Insertar", f"Valor {value} insertado en el árbol.")
            self.draw_tree()
        else:
            messagebox.showwarning("Advertencia", "Ingrese un valor numérico.")

    def search_value(self):
        value = self.entry.get()
        if value.isdigit():
            result = search(self.tree, int(value))
            if result:
                messagebox.showinfo("Buscar", f"Valor {value} encontrado en el árbol.")
            else:
                messagebox.showinfo("Buscar", f"Valor {value} no encontrado en el árbol.")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un valor numérico.")

    def draw_tree(self):
        self.canvas.delete("all")
        if self.tree:
            self._draw_node(self.tree, 400, 30, 200)

    def _draw_node(self, node, x, y, dx):
        if node:
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.val), font=("Arial", 12, "bold"))
            if node.left:
                self.canvas.create_line(x-20, y+20, x-dx+20, y+80-20)
                self._draw_node(node.left, x-dx, y+80, dx//2)
            if node.right:
                self.canvas.create_line(x+20, y+20, x+dx-20, y+80-20)
                self._draw_node(node.right, x+dx, y+80, dx//2)

if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()
