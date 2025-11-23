#!/usr/bin/env python3
"""
Demo de validación de email - Archivo principal para ejecutar
"""

import sys
import os

# Agregar el directorio actual al path para importar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from tkinter import ttk, messagebox
from validaciones_utils import ValidacionesUtils

# Importar las clases de ejemplo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ejemplos_uso_validacion import ClienteInterface, ProveedorInterface, EmpleadoInterface


def crear_interfaz_demo():
    """
    Crea una interfaz de demostración completa
    """
    root = tk.Tk()
    root.title("Sistema de Validación de Email - Demo")
    root.geometry("800x600")
    
    # Configurar el estilo
    style = ttk.Style()
    style.theme_use('clam')
    
    # Frame principal
    main_frame = tk.Frame(root, bg='#f5f5f5')
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Título
    title_label = tk.Label(main_frame, text="Sistema de Validación de Email", 
                          font=('Arial', 16, 'bold'), bg='#f5f5f5')
    title_label.pack(pady=10)
    
    # Notebook para las diferentes pestañas
    notebook = ttk.Notebook(main_frame)
    notebook.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Pestaña de validación básica
    frame_validacion = tk.Frame(notebook, bg='white')
    notebook.add(frame_validacion, text="Validación Básica")
    crear_pestana_validacion_basica(frame_validacion)
    
    # Pestaña de Cliente
    frame_cliente = tk.Frame(notebook, bg='white')
    notebook.add(frame_cliente, text="Gestión de Clientes")
    ClienteInterface(frame_cliente)
    
    # Pestaña de Proveedor
    frame_proveedor = tk.Frame(notebook, bg='white')
    notebook.add(frame_proveedor, text="Gestión de Proveedores")
    ProveedorInterface(frame_proveedor)
    
    # Pestaña de Empleado
    frame_empleado = tk.Frame(notebook, bg='white')
    notebook.add(frame_empleado, text="Gestión de Empleados")
    EmpleadoInterface(frame_empleado)
    
    # Frame de información
    info_frame = tk.Frame(main_frame, bg='#e8f4f8', relief='groove', bd=1)
    info_frame.pack(fill='x', padx=10, pady=5)
    
    tk.Label(info_frame, text="Información:", font=('Arial', 10, 'bold'), 
            bg='#e8f4f8').pack(anchor='w', padx=5, pady=2)
    
    info_text = """
    • La validación de email se realiza automáticamente cuando el campo pierde el foco
    • También puedes usar el botón 'Validar Email' para validar manualmente
    • El formato válido es: usuario@dominio.com
    • Se permiten letras, números, puntos, guiones y guiones bajos
    """
    
    tk.Label(info_frame, text=info_text, justify='left', bg='#e8f4f8', 
            font=('Arial', 9)).pack(anchor='w', padx=5, pady=2)
    
    return root


def crear_pestana_validacion_basica(parent):
    """
    Crea la pestaña de validación básica
    """
    # Frame principal
    main_frame = tk.Frame(parent, bg='white')
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)
    
    # Email a validar
    tk.Label(main_frame, text="Email a validar:", bg='white', 
            font=('Arial', 12)).grid(row=0, column=0, sticky='w', pady=10)
    
    entry_email = tk.Entry(main_frame, width=40, font=('Arial', 12))
    entry_email.grid(row=0, column=1, pady=10, padx=10)
    
    # Variable para mostrar el resultado
    var_resultado = tk.StringVar()
    var_resultado.set("Ingrese un email y presione Validar")
    
    # Label para mostrar el resultado
    lbl_resultado = tk.Label(main_frame, textvariable=var_resultado, 
                           bg='white', font=('Arial', 11), fg='blue')
    lbl_resultado.grid(row=1, column=0, columnspan=2, pady=10)
    
    def validar_email_demo():
        """Función para validar el email de demo"""
        email = entry_email.get()
        
        if not email.strip():
            var_resultado.set("Por favor ingrese un email")
            lbl_resultado.config(fg='red')
            return
        
        # Validar usando nuestra función
        if ValidacionesUtils.validar_email(email):
            var_resultado.set(f"✓ El email '{email}' es VÁLIDO")
            lbl_resultado.config(fg='green')
        else:
            var_resultado.set(f"✗ El email '{email}' es INVÁLIDO")
            lbl_resultado.config(fg='red')
    
    # Botón para validar
    tk.Button(main_frame, text="Validar Email", command=validar_email_demo,
             bg='#4CAF50', fg='white', font=('Arial', 11), 
             padx=20, pady=5).grid(row=2, column=0, columnspan=2, pady=20)
    
    # Frame de ejemplos
    ejemplos_frame = tk.Frame(main_frame, bg='#f9f9f9', relief='groove', bd=1)
    ejemplos_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')
    
    tk.Label(ejemplos_frame, text="Ejemplos de emails:", bg='#f9f9f9', 
            font=('Arial', 10, 'bold')).pack(anchor='w', padx=10, pady=5)
    
    ejemplos = [
        "usuario@dominio.com - Válido",
        "user.name@example.com - Válido", 
        "user-name@domain.co.uk - Válido",
        "usuario@dominio - Inválido (sin extensión)",
        "usuario@ - Inválido (sin dominio)",
        "@dominio.com - Inválido (sin usuario)",
        "usuario dominio.com - Inválido (sin @)"
    ]
    
    for ejemplo in ejemplos:
        tk.Label(ejemplos_frame, text=f"• {ejemplo}", bg='#f9f9f9', 
                font=('Arial', 9)).pack(anchor='w', padx=20, pady=2)


def main():
    """
    Función principal
    """
    try:
        root = crear_interfaz_demo()
        root.mainloop()
    except Exception as e:
        print(f"Error al ejecutar la demo: {e}")
        messagebox.showerror("Error", f"Error al ejecutar la demo: {e}")


if __name__ == "__main__":
    main()