import re
import tkinter as tk
from tkinter import messagebox

class ValidacionesUtils:
    """
    Clase con métodos estáticos para validaciones comunes
    """
    
    @staticmethod
    def validar_email(email):
        """
        Valida el formato de un email usando regex
        
        Args:
            email (str): El email a validar
            
        Returns:
            bool: True si el email es válido, False si no
        """
        if not email or not isinstance(email, str):
            return False
            
        # Patrón regex para validar email
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Verificar que el email coincida con el patrón
        if re.match(patron_email, email.strip()):
            return True
        else:
            return False
    
    @staticmethod
    def validar_email_con_gui(email, parent_window=None, mostrar_error=True):
        """
        Valida email y muestra mensaje de error en GUI si es necesario
        
        Args:
            email (str): El email a validar
            parent_window: Ventana padre para el mensaje de error
            mostrar_error (bool): Si mostrar o no el mensaje de error
            
        Returns:
            bool: True si el email es válido, False si no
        """
        if not email.strip():
            if mostrar_error:
                messagebox.showerror("Error de Validación", 
                                   "El campo de email no puede estar vacío.", 
                                   parent=parent_window)
            return False
            
        if not ValidacionesUtils.validar_email(email):
            if mostrar_error:
                messagebox.showerror("Error de Validación", 
                                   f"El email '{email}' no tiene un formato válido.\n\n"
                                   "Formato esperado: usuario@dominio.com", 
                                   parent=parent_window)
            return False
            
        return True
    
    @staticmethod
    def validar_telefono(telefono):
        """
        Valida formato de número de teléfono (opcional)
        
        Args:
            telefono (str): El número de teléfono a validar
            
        Returns:
            bool: True si el teléfono es válido o está vacío, False si no
        """
        if not telefono.strip():
            return True  # Permitir vacío
            
        # Patrón para teléfonos: puede incluir +, números, espacios, guiones y paréntesis
        patron_telefono = r'^[\+]?[0-9\s\-\(\)]+$'
        
        return bool(re.match(patron_telefono, telefono.strip()))
    
    @staticmethod
    def validar_solo_letras(texto, permitir_espacios=True):
        """
        Valida que el texto contenga solo letras
        
        Args:
            texto (str): El texto a validar
            permitir_espacios (bool): Si permitir o no espacios
            
        Returns:
            bool: True si el texto es válido, False si no
        """
        if not texto.strip():
            return False
            
        if permitir_espacios:
            patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
        else:
            patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$'
            
        return bool(re.match(patron, texto.strip()))
    
    @staticmethod
    def validar_no_vacio(valor, nombre_campo="El campo"):
        """
        Valida que un valor no esté vacío
        
        Args:
            valor (str): El valor a validar
            nombre_campo (str): Nombre del campo para el mensaje de error
            
        Returns:
            bool: True si no está vacío, False si no
        """
        return bool(valor and valor.strip())


# Función auxiliar para crear validadores de email en diferentes clases
def crear_validador_email(entry_widget, parent_window=None):
    """
    Crea una función de validación de email para un Entry widget específico
    
    Args:
        entry_widget: El widget Entry de tkinter
        parent_window: Ventana padre para mensajes de error
        
    Returns:
        function: Función de validación que puede ser llamada
    """
    def validar():
        email = entry_widget.get()
        return ValidacionesUtils.validar_email_con_gui(email, parent_window)
    
    return validar