import tkinter as tk
from tkinter import ttk

class MenuArbolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú en forma de árbol")
        self.geometry("400x300")
        self._crear_treeview()

    def _crear_treeview(self):
        # Crear el widget Treeview
        self.tree = ttk.Treeview(self)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Insertar nodos raíz
        menu_archivo = self.tree.insert("", "end", text="Archivo", open=True)
        menu_edicion = self.tree.insert("", "end", text="Edición", open=True)
        menu_ayuda = self.tree.insert("", "end", text="Ayuda", open=True)

        # Submenús de "Archivo"
        self.tree.insert(menu_archivo, "end", text="Nuevo")
        self.tree.insert(menu_archivo, "end", text="Abrir")
        self.tree.insert(menu_archivo, "end", text="Guardar")

        # Submenús de "Edición"
        self.tree.insert(menu_edicion, "end", text="Copiar")
        self.tree.insert(menu_edicion, "end", text="Pegar")
        self.tree.insert(menu_edicion, "end", text="Cortar")

        # Submenús de "Ayuda"
        self.tree.insert(menu_ayuda, "end", text="Documentación")
        self.tree.insert(menu_ayuda, "end", text="Acerca de")

        # Evento opcional: mostrar selección
        self.tree.bind("<<TreeviewSelect>>", self._mostrar_seleccion)

    def _mostrar_seleccion(self, event):
        item_id = self.tree.selection()[0]
        print("Seleccionaste:", self.tree.item(item_id)["text"])

if __name__ == "__main__":
    app = MenuArbolApp()
    app.mainloop()
