import tkinter as tk
from tkinter import ttk

# Datos de ejemplo
reporte_datos = [
    {"ID": 1, "Modelo": "BMW 3 Series", "Año": 2023, "Color": "Negro", "Transmisión": "Automática"},
    {"ID": 2, "Modelo": "BMW X5", "Año": 2022, "Color": "Blanco", "Transmisión": "Manual"},
    {"ID": 3, "Modelo": "BMW 5 Series", "Año": 2024, "Color": "Gris", "Transmisión": "Automática"},
]

# Ventana principal
root = tk.Tk()
root.title("Reporte de Autos")
root.geometry("700x300")

# Frame para la tabla
tabla_frame = tk.Frame(root)
tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Crear Treeview como tabla
tabla = ttk.Treeview(tabla_frame, columns=("ID", "Modelo", "Año", "Color", "Transmisión"), show="headings")
tabla.pack(fill="both", expand=True)

# Definir encabezados
for col in ("ID", "Modelo", "Año", "Color", "Transmisión"):
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=100)

# Insertar datos
for fila in reporte_datos:
    tabla.insert("", "end", values=(fila["ID"], fila["Modelo"], fila["Año"], fila["Color"], fila["Transmisión"]))

# Scroll vertical
scroll = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

root.mainloop()
