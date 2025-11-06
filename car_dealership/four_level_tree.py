import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ArbolCuatroNiveles:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Árbol de 4 niveles")
        self.window.geometry("500x400")

        self.tree = ttk.Treeview(self.window)
        self.tree.pack(fill="both", expand=True)

        # Nivel 1
        vehiculos_id = self.tree.insert("", "end", iid="vehiculos", text="Vehículos")

        # Nivel 2
        autos_id = self.tree.insert(vehiculos_id, "end", iid="autos", text="Autos")

        # Nivel 3
        bmw_id = self.tree.insert(autos_id, "end", iid="bmw", text="BMW")

        # Nivel 4
        self.tree.insert(bmw_id, "end", iid="bmw3", text="BMW 3 Series")
        self.tree.insert(bmw_id, "end", iid="bmw5", text="BMW 5 Series")

        # Otro ejemplo paralelo
        suvs_id = self.tree.insert(vehiculos_id, "end", iid="suvs", text="SUVs")
        audi_id = self.tree.insert(suvs_id, "end", iid="audi", text="Audi")
        self.tree.insert(audi_id, "end", iid="q5", text="Audi Q5")

        # Asociar evento
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.window.mainloop()

    def on_select(self, event):
        selected = self.tree.focus()
        texto = self.tree.item(selected, "text")
        nivel = self.get_nivel(selected)
        messagebox.showinfo("Selección", f"Seleccionaste: {texto}\nNivel: {nivel}")

    def get_nivel(self, item_id):
        nivel = 0
        while item_id:
            item_id = self.tree.parent(item_id)
            nivel += 1
        return nivel

ArbolCuatroNiveles()
