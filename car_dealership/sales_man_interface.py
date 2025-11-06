import data
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import ttk
from car_interface import Car_interface

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

        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="New Employee",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # Id
        lbl_id = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Employee Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Entry(self.new_label_frame, width=20)
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

        # Email
        lbl_email = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Email: ')
        lbl_email.place(x=20, y=90)
        self.txt_email = tk.Entry(self.new_label_frame, width=20)
        self.txt_email.place(x=120, y=90)

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

        # Salary
        lbl_salary = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Salary: ')
        lbl_salary.place(x=20, y=150)
        self.txt_salary = tk.Entry(self.new_label_frame, width=20)
        self.txt_salary.place(x=120, y=150)

        # Buttons
        self.btn_add_employee = tk.Button(self.new_label_frame, text="Add Employee", width=18)
        self.btn_add_employee.place(x=450, y=280)
        self.new_frame.place(x=0, y=0)
