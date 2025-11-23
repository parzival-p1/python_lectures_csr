import tkinter as tk
from tkinter import PhotoImage

def accion():
    print("¡Botón activado!")

# Crear ventana principal
root = tk.Tk()
root.title("Botón con imagen y texto")

# Cargar imagen (usa una imagen .gif o .png compatible)
imagen = PhotoImage(file="./img/bmw-logo.png")  # Asegúrate de que el archivo exista

# Crear botón con imagen y texto
boton = tk.Button(
    root,
    image=imagen,
    text="Haz clic aquí",
    compound="left",  # Imagen a la izquierda del texto
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5,
    command=accion,
    relief="raised",
    bg="#f0f0f0",
    activebackground="#d0d0d0"
)

boton.pack(pady=20)

root.mainloop()
