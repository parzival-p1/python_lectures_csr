import data
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import ttk
from car_interface import Car_interface
from validaciones_utils import ValidacionesUtils, crear_validador_email

class Sales_man_interface:
    def __init__(self, Data, content_frame, bottom_frame):
        self.data = Data
        self.content_frame = content_frame
        self.bottom_frame = bottom_frame
        self.content_frame.update_idletasks()  # Asegura que el layout esté calculado
        self.bottom_frame.update_idletasks()  # Asegura que el layout esté calculado

    def update_models(self, event):
        brand = self.txt_brand.get()
        models = self.models.get(brand, [])
        self.txt_model.set('')  # clean field
        self.txt_model['values'] = models

    def new_employee(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="New Employee",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        self.new_frame.place(x=0, y=0)

        # Id
        lbl_id = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Employee Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Entry(self.new_label_frame, width=20)
        self.txt_id.insert(0, str(self.data.get_next_salesman_id()))
        self.txt_id.config(state='readonly')
        self.txt_id.place(x=120, y=20)

        # Name
        lbl_name = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='First Name: ')
        lbl_name.place(x=20, y=60)
        self.txt_name = tk.Entry(self.new_label_frame, width=20)
        self.txt_name.place(x=120, y=60)

        # Last Name
        lbl_last_name = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Last Name: ')
        lbl_last_name.place(x=350, y=60)
        self.txt_last_name = tk.Entry(self.new_label_frame, width=20)
        self.txt_last_name.place(x=450, y=60)

        # Email - con validación mejorada
        lbl_email = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Email: ')
        lbl_email.place(x=20, y=90)
        self.txt_email = tk.Entry(self.new_label_frame, width=20)
        self.txt_email.place(x=120, y=90)
        
        # Agregar validación cuando el campo pierde el foco
        self.txt_email.bind('<FocusOut>', self.validar_email_perdida_foco)

        # Phone number
        lbl_phone_number = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Phone Number: ')
        lbl_phone_number.place(x=350, y=90)
        self.txt_phone_number = tk.Entry(self.new_label_frame, width=20)
        self.txt_phone_number.place(x=450, y=90)

        # Address
        lbl_address = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Address: ')
        lbl_address.place(x=20, y=120)
        self.txt_address = tk.Entry(self.new_label_frame, width=20)
        self.txt_address.place(x=120, y=120)

        # Birthday
        lbl_birthday = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Birthday: ')
        lbl_birthday.place(x=350, y=120)
        self.txt_bday = DateEntry(self.new_label_frame, width=20,  background='#4595BE', foreground='white', borderwidth=2,
                          date_pattern='dd/mm/yyyy')
        self.txt_bday.place(x=450, y=120)

        # Gender
        lbl_gender = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Gender: ')
        lbl_gender.place(x=20, y=150)
        self.txt_gender = ttk.Combobox(self.new_label_frame, width=20, values=["Female", "Male", "Other"], state='readonly')
        self.txt_gender.place(x=120, y=150)

        # Salary
        lbl_salary = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Salary: ')
        lbl_salary.place(x=350, y=150)
        self.txt_salary = tk.Entry(self.new_label_frame, width=20)
        self.txt_salary.place(x=450, y=150)

        # Buttons
        self.btn_add_employee = tk.Button(self.new_label_frame, text="Add Employee", width=18, command=self.add_new_salesman)
        self.btn_add_employee.place(x=450, y=280)
        self.new_frame.place(x=0, y=0)

    def validar_email_perdida_foco(self, event=None):
        """
        Valida el email cuando el campo pierde el foco
        """
        email = self.txt_email.get()
        if email.strip():  # Solo validar si hay contenido
            ValidacionesUtils.validar_email_con_gui(email, self.content_frame, mostrar_error=True)

    def add_new_salesman(self):
        """
        Agrega un nuevo vendedor con validación completa
        """
        if self.validate_salesman_info():
            # Aquí iría la lógica para guardar el vendedor
            messagebox.showinfo("Éxito!", "El nuevo cliente se ha añadido!")
            self.clear_fields()
        else:
            messagebox.showerror("Error!", "Por favor corrige los errores antes de continuar.")

    def validate_salesman_info(self):
        """
        Valida toda la información del vendedor
        """
        # Validar campos vacíos
        campos = [
            (self.txt_name.get(), "Nombre"),
            (self.txt_last_name.get(), "Apellido"),
            (self.txt_email.get(), "Email"),
            (self.txt_phone_number.get(), "Teléfono"),
            (self.txt_address.get(), "Dirección"),
            (self.txt_bday.get(), "Fecha de nacimiento"),
            (self.txt_gender.get(), "Género")
        ]
        
        for valor, campo in campos:
            if not ValidacionesUtils.validar_no_vacio(valor, campo):
                messagebox.showerror("ERROR!!!", f"El campo {campo} no puede estar vacío!")
                return False
        
        # Validar formato del email
        if not ValidacionesUtils.validar_email(self.txt_email.get()):
            messagebox.showerror("ERROR!!!", 
                               f"El email '{self.txt_email.get()}' no tiene un formato válido.\n\n"
                               "Formato esperado: usuario@dominio.com")
            return False
        
        # Validar formato del teléfono
        if not ValidacionesUtils.validar_telefono(self.txt_phone_number.get()):
            messagebox.showerror("ERROR!!!", 
                               "El número de teléfono contiene caracteres no válidos.")
            return False
        
        # Validar que el nombre solo contenga letras
        if not ValidacionesUtils.validar_solo_letras(self.txt_name.get()):
            messagebox.showerror("ERROR!!!", 
                               "El nombre solo puede contener letras y espacios.")
            return False
            
        if not ValidacionesUtils.validar_solo_letras(self.txt_last_name.get()):
            messagebox.showerror("ERROR!!!", 
                               "El apellido solo puede contener letras y espacios.")
            return False
        
        return True

    def clear_fields(self):
        """
        Limpia todos los campos del formulario
        """
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.insert(0, str(self.data.get_next_salesman_id()))
        self.txt_id.config(state='readonly')
        
        self.txt_gender.set('')
        self.txt_phone_number.delete(0, tk.END)
        self.txt_name.delete(0, tk.END)
        self.txt_last_name.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_address.delete(0, tk.END)
        self.txt_bday.delete(0, tk.END)
        self.txt_salary.delete(0, tk.END)