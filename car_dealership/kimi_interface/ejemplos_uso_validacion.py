"""
Ejemplos de uso de las funciones de validación de email en diferentes clases
"""

import tkinter as tk
from tkinter import messagebox, ttk
from validaciones_utils import ValidacionesUtils, crear_validador_email


class ClienteInterface:
    """
    Ejemplo de uso en una interfaz de gestión de clientes
    """
    
    def __init__(self, parent_window):
        self.parent = parent_window
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.parent, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Email
        tk.Label(main_frame, text="Email del Cliente:").grid(row=0, column=0, sticky='w', pady=5)
        self.txt_email = tk.Entry(main_frame, width=30)
        self.txt_email.grid(row=0, column=1, pady=5, padx=5)
        
        # Opción 1: Validación con bind
        self.txt_email.bind('<FocusOut>', self.validar_email_perdida_foco)
        
        # Opción 2: Validación con botón
        tk.Button(main_frame, text="Validar Email", 
                 command=self.validar_email_boton).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Opción 3: Usar el creador de validadores
        self.validador_email = crear_validador_email(self.txt_email, self.parent)
        tk.Button(main_frame, text="Validar con Función Creada", 
                 command=self.validador_email).grid(row=2, column=0, columnspan=2, pady=10)
    
    def validar_email_perdida_foco(self, event=None):
        """Validación cuando el campo pierde el foco"""
        email = self.txt_email.get()
        if email.strip():
            ValidacionesUtils.validar_email_con_gui(email, self.parent)
    
    def validar_email_boton(self):
        """Validación con botón"""
        email = self.txt_email.get()
        if ValidacionesUtils.validar_email_con_gui(email, self.parent):
            messagebox.showinfo("Validación Exitosa", "El email es válido!")


class ProveedorInterface:
    """
    Ejemplo de uso en una interfaz de gestión de proveedores
    """
    
    def __init__(self, parent_window):
        self.parent = parent_window
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.parent, bg='#e8f4f8')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Email de contacto
        tk.Label(main_frame, text="Email de Contacto:").grid(row=0, column=0, sticky='w', pady=5)
        self.txt_email_contacto = tk.Entry(main_frame, width=30)
        self.txt_email_contacto.grid(row=0, column=1, pady=5, padx=5)
        
        # Email de facturación
        tk.Label(main_frame, text="Email de Facturación:").grid(row=1, column=0, sticky='w', pady=5)
        self.txt_email_facturacion = tk.Entry(main_frame, width=30)
        self.txt_email_facturacion.grid(row=1, column=1, pady=5, padx=5)
        
        # Botón para validar ambos emails
        tk.Button(main_frame, text="Validar Emails", 
                 command=self.validar_emails_proveedor).grid(row=2, column=0, columnspan=2, pady=10)
    
    def validar_emails_proveedor(self):
        """Valida ambos emails del proveedor"""
        email_contacto = self.txt_email_contacto.get()
        email_facturacion = self.txt_email_facturacion.get()
        
        # Validar email de contacto
        if not ValidacionesUtils.validar_email_con_gui(email_contacto, self.parent):
            return False
        
        # Validar email de facturación
        if not ValidacionesUtils.validar_email_con_gui(email_facturacion, self.parent):
            return False
        
        # Verificar que sean diferentes (opcional)
        if email_contacto == email_facturacion:
            respuesta = messagebox.askyesno(
                "Emails Iguales",
                "Los emails de contacto y facturación son iguales. ¿Desea continuar?"
            )
            if not respuesta:
                return False
        
        messagebox.showinfo("Validación Exitosa", "Ambos emails son válidos!")
        return True


class EmpleadoInterface:
    """
    Ejemplo de uso en una interfaz de gestión de empleados
    """
    
    def __init__(self, parent_window):
        self.parent = parent_window
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.parent, bg='#fff2e6')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Información personal
        tk.Label(main_frame, text="Email Personal:").grid(row=0, column=0, sticky='w', pady=5)
        self.txt_email_personal = tk.Entry(main_frame, width=30)
        self.txt_email_personal.grid(row=0, column=1, pady=5, padx=5)
        
        # Email corporativo
        tk.Label(main_frame, text="Email Corporativo:").grid(row=1, column=0, sticky='w', pady=5)
        self.txt_email_corporativo = tk.Entry(main_frame, width=30)
        self.txt_email_corporativo.grid(row=1, column=1, pady=5, padx=5)
        
        # Dominio corporativo
        dominios = ["@empresa.com", "@corp.empresa.com", "@ventas.empresa.com"]
        self.var_dominio = tk.StringVar()
        self.var_dominio.set(dominios[0])
        
        tk.Label(main_frame, text="Dominio:").grid(row=1, column=2, sticky='w', pady=5, padx=(20, 5))
        ttk.Combobox(main_frame, textvariable=self.var_dominio, values=dominios, 
                    width=15, state='readonly').grid(row=1, column=3, pady=5)
        
        # Botones
        tk.Button(main_frame, text="Generar Email Corporativo", 
                 command=self.generar_email_corporativo).grid(row=2, column=0, columnspan=2, pady=10)
        
        tk.Button(main_frame, text="Validar Todo", 
                 command=self.validar_todo).grid(row=2, column=2, columnspan=2, pady=10)
    
    def generar_email_corporativo(self):
        """Genera el email corporativo basado en el nombre"""
        # Aquí normalmente obtendrías el nombre del empleado
        nombre = "juan.perez"  # Ejemplo
        dominio = self.var_dominio.get()
        email_corporativo = f"{nombre}{dominio}"
        
        self.txt_email_corporativo.delete(0, tk.END)
        self.txt_email_corporativo.insert(0, email_corporativo)
    
    def validar_todo(self):
        """Valida todos los campos de email"""
        email_personal = self.txt_email_personal.get()
        email_corporativo = self.txt_email_corporativo.get()
        
        # Validar que al menos uno tenga contenido
        if not email_personal.strip() and not email_corporativo.strip():
            messagebox.showerror("Error", "Debe proporcionar al menos un email.")
            return False
        
        # Validar email personal si existe
        if email_personal.strip():
            if not ValidacionesUtils.validar_email_con_gui(email_personal, self.parent):
                return False
        
        # Validar email corporativo si existe
        if email_corporativo.strip():
            if not ValidacionesUtils.validar_email_con_gui(email_corporativo, self.parent):
                return False
        
        messagebox.showinfo("Validación Exitosa", "Validación completada exitosamente!")
        return True


# Función para demostrar el uso de las validaciones
def demo_validaciones():
    """
    Función de demostración que muestra cómo usar las validaciones
    """
    root = tk.Tk()
    root.title("Demo de Validaciones de Email")
    root.geometry("600x400")
    
    # Crear notebook (pestañas)
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Pestaña de Cliente
    frame_cliente = tk.Frame(notebook)
    notebook.add(frame_cliente, text="Cliente")
    ClienteInterface(frame_cliente)
    
    # Pestaña de Proveedor
    frame_proveedor = tk.Frame(notebook)
    notebook.add(frame_proveedor, text="Proveedor")
    ProveedorInterface(frame_proveedor)
    
    # Pestaña de Empleado
    frame_empleado = tk.Frame(notebook)
    notebook.add(frame_empleado, text="Empleado")
    EmpleadoInterface(frame_empleado)
    
    root.mainloop()


if __name__ == "__main__":
    demo_validaciones()