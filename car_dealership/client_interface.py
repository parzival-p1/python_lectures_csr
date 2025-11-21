import re

import pandas as pd

import data
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import ttk
from sales_man_interface import Sales_man_interface

class Client_interface:
    def __init__(self, Data, content_frame, bottom_frame):
        self.data = Data
        self.content_frame = content_frame
        self.bottom_frame = bottom_frame
        self.content_frame.update_idletasks()  # Asegura que el layout esté calculado
        self.bottom_frame.update_idletasks()  # Asegura que el layout esté calculado

    def new_client(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="New Client",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # New Client
        self.new_frame.place(x=0, y=0)

        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="New Client",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # Id
        lbl_id = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Client Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Entry(self.new_label_frame, width=20)
        self.txt_id.insert(0, str(self.data.get_next_client_id()))
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

        # Gender
        lbl_gender = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Gender: ')
        lbl_gender.place(x=20, y=150)
        self.txt_gender = ttk.Combobox(self.new_label_frame, width=20, values=["Female", "Male", "Other"], state='readonly')
        self.txt_gender.place(x=120, y=150)

        # Buttons
        self.btn_add_employee = tk.Button(self.new_label_frame, text="Add Client", width=18, command=self.add_new_client)
        self.btn_add_employee.place(x=450, y=280)
        self.new_frame.place(x=0, y=0)

    def add_new_client(self): # 'ID', 'Name', 'Last Name', 'Phone Number', 'Address', 'Email', 'Gender', 'Birthday'
        if (self.validate_client_info()):
            client_dict = {
                'ID': self.txt_id.get(),
                'Name': self.txt_name.get(),
                'Last Name': self.txt_last_name.get(),
                'Phone Number': self.txt_phone_number.get(),
                'Address': self.txt_address.get(),
                'Email': self.txt_email.get(),
                'Gender': self.txt_gender.get(),
                'Birthday': self.txt_bday.get()
            }
            self.data.add_client(client_dict)
            messagebox.showinfo("Exito!", "El nuevo cliente se ha añadido!")
            self.clear_fields()
        else:
            messagebox.showinfo("Mal!", "Algo anda mal")

    def validate_client_info(self):
        # no validar, precio, km, stock, y id
        regex = r"[+-]?[0-9]+\.[0-9]+"
        if (self.txt_name.get() == "" or self.txt_last_name.get() == "" or self.txt_email.get() == ""
                or self.txt_phone_number.get() == "" or self.txt_address.get() == "" or self.txt_bday.get() == ""
                or self.txt_gender.get() == "" or self.txt_id.get() == ""):
            messagebox.showerror("ERROR!!!", "Los campos no pueden estar vacios!")
            return False

        if not self.validate_email(self.txt_email.get()):
            messagebox.showerror("ERROR!!!", "El email no tiene un formato valido")
            return False
        return True

    def validate_email(self, email: str) -> bool:
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None

    def clear_fields(self):
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.insert(0, str(self.data.get_next_client_id()))
        self.txt_id.config(state='readonly')
        self.txt_gender.set('')

        self.txt_phone_number.delete(0, tk.END)
        self.txt_name.delete(0, tk.END)
        self.txt_last_name.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_address.delete(0, tk.END)
        self.txt_bday.delete(0, tk.END)
