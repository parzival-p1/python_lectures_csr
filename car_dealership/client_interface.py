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

    def delete_client(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="Delete Client",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # select client
        lbl_select_client = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Select client: ')
        lbl_select_client.place(x=20, y=60)
        self.txt_select_client = ttk.Combobox(self.new_label_frame, width=18, state="readonly",
                                           values=self.data.df_clients["ID"].tolist())
        self.txt_select_client.place(x=120, y=60)

        # Buttons
        self.btn_select_client = tk.Button(self.new_label_frame, text="Select Client", width=15,
                                        command=self.show_delete_details)
        self.btn_select_client.place(x=300, y=60)

        # Separator
        separator = tk.Frame(self.new_label_frame, bg='white', height=2, width=self.content_frame.winfo_width() -30)
        separator.place(x=10, y=120)
        self.client_details = tk.Frame(self.new_label_frame, bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 30,
                                             height = self.content_frame.winfo_height() - 180)

        # Client details
        lbl_id = tk.Label(self.client_details, text="ID: ", bg='#484b4c', fg='white')
        lbl_id.place(x=20, y=10)
        self.lbl_id = tk.Label(self.client_details, text="12345", bg='#484b4c', fg="white")
        self.lbl_id.place(x=120, y=10)

        lbl_name = tk.Label(self.client_details, text="Name: ", bg='#484b4c', fg='white')
        lbl_name.place(x=20, y=30)
        self.lbl_name = tk.Label(self.client_details, text="Name", bg='#484b4c', fg='white')
        self.lbl_name.place(x=120, y=30)

        lbl_last_name = tk.Label(self.client_details, text="Last name: ", bg='#484b4c', fg='white')
        lbl_last_name.place(x=20, y=50)
        self.lbl_last_name = tk.Label(self.client_details, text="2000", bg='#484b4c', fg='white')
        self.lbl_last_name.place(x=120, y=50)

        lbl_phone_number = tk.Label(self.client_details, text="Phone Number: ", bg='#484b4c', fg='white')
        lbl_phone_number.place(x=20, y=70)
        self.lbl_phone_number = tk.Label(self.client_details, text="Phone Number", bg='#484b4c', fg='white')
        self.lbl_phone_number.place(x=120, y=70)

        lbl_address = tk.Label(self.client_details, text="Address: ", bg='#484b4c', fg='white')
        lbl_address.place(x=20, y=90)
        self.lbl_address = tk.Label(self.client_details, text="Address", bg='#484b4c', fg='white')
        self.lbl_address.place(x=120, y=90)

        lbl_email = tk.Label(self.client_details, text="Email: ", bg='#484b4c', fg='white')
        lbl_email.place(x=20, y=110)
        self.lbl_email = tk.Label(self.client_details, text="Email", bg='#484b4c', fg='white')
        self.lbl_email.place(x=120, y=110)

        lbl_gender = tk.Label(self.client_details, text="Gender: ", bg='#484b4c', fg='white')
        lbl_gender.place(x=20, y=130)
        self.lbl_gender = tk.Label(self.client_details, text="Gender", bg='#484b4c', fg='white')
        self.lbl_gender.place(x=120, y=130)

        lbl_birthday = tk.Label(self.client_details, text="Birthday: ", bg='#484b4c', fg='white')
        lbl_birthday.place(x=20, y=150)
        self.lbl_birthday = tk.Label(self.client_details, text="Birthday", bg='#484b4c', fg='white')
        self.lbl_birthday.place(x=120, y=150)

        # Delete Button
        self.btn_delete_client = tk.Button(self.client_details, text="Delete Client", width=15,
                                           command=self.confirm_delete_client)
        self.btn_delete_client.place(x=600, y=250)

        self.new_frame.place(x=0, y=0)

    def show_delete_details(self):
        if self.txt_select_client.get() != "":
            self.client_details.place(x=10, y=130)  # 'ID', 'Name', 'Last Name', 'Phone Number', 'Address', 'Email', 'Gender', 'Birthday'
            df_client = self.data.get_client_data_by_id(self.txt_select_client.get())
            self.lbl_id.config(text= df_client['ID'].iloc[0])
            self.lbl_name.config(text=df_client['Name'].iloc[0])
            self.lbl_last_name.config(text=df_client['Last Name'].iloc[0])
            self.lbl_phone_number.config(text=df_client['Phone Number'].iloc[0])
            self.lbl_address.config(text=df_client['Address'].iloc[0])
            self.lbl_email.config(text=df_client['Email'].iloc[0])
            self.lbl_gender.config(text=df_client['Gender'].iloc[0])
            self.lbl_birthday.config(text=df_client['Birthday'].iloc[0])
        else:
            messagebox.showerror("Error!!!", "No se ha seleccionado ningun Cliente")

    def confirm_delete_client(self):
        answer = messagebox.askyesno("Confirmar borrado", "Desea borrar el cliente? "
                                                          "(esta opcion no se puede deshacer)")
        if answer:
            self.data.delete_client_by_id(self.txt_select_client.get())
            self.txt_select_client["values"] = values=self.data.df_clients["ID"].tolist()
            if len(values) > 0:
                self.txt_select_client.current(0)
            else:
                self.txt_select_client.set("")
            self.client_details.place_forget()
            messagebox.showinfo("Borrado exitoso!", "El cliente se ha eliminado con exito!!!")
        else:
            messagebox.showinfo("Sin cambios", "No se realizo ningun cambio.")

    def edit_client(self): # 'ID', 'Name', 'Last Name', 'Phone Number', 'Address', 'Email', 'Gender', 'Birthday'
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height=self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="Edit Car",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height=self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # select car
        lbl_select_client = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Select client: ')
        lbl_select_client.place(x=20, y=60)
        self.txt_select_client = ttk.Combobox(self.new_label_frame, width=18, state="readonly",
                                           values=self.data.df_clients["ID"].tolist())
        self.txt_select_client.place(x=120, y=60)

        # Buttons
        self.btn_select_client = tk.Button(self.new_label_frame, text="Select Client", width=15,
                                        command=self.show_edit_details)
        self.btn_select_client.place(x=300, y=60)

        # Separator
        separator = tk.Frame(self.new_label_frame, bg='white', height=2, width=self.content_frame.winfo_width() - 30)
        separator.place(x=10, y=120)
        self.client_details = tk.Frame(self.new_label_frame, bg='#484b4c',
                                    width=self.content_frame.winfo_width() - 30,
                                    height=self.content_frame.winfo_height() - 180)
        # Client details
        # Id
        lbl_id = tk.Label(self.client_details, bg='#484b4c', fg="white", text='Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Entry(self.client_details, width=20)
        self.txt_id.insert(0, str(self.data.get_next_client_id()))
        self.txt_id.config(state='readonly')
        self.txt_id.place(x=120, y=20)

        # Name
        lbl_name = tk.Label(self.client_details, bg='#484b4c', fg="white", text='Name: ')
        lbl_name.place(x=20, y=60)
        self.txt_name = tk.Entry(self.client_details, width=18)
        self.txt_name.place(x=120, y=60)

        # Last name
        lbl_last_name = tk.Label(self.client_details, bg='#484b4c', fg="white", text='Last name: ')
        lbl_last_name.place(x=350, y=60)
        self.txt_last_name = tk.Entry(self.client_details, width=18)
        self.txt_last_name.place(x=450, y=60)

        # Phone number
        lbl_phone_number = tk.Label(self.client_details, bg='#484b4c', fg="white", text='Phone number: ')
        lbl_phone_number.place(x=20, y=90)
        self.txt_phone_number = tk.Entry(self.client_details, width=18)
        self.txt_phone_number.place(x=120, y=90)

        # Address
        lbl_color = tk.Label(self.client_details, bg='#484b4c', fg="white", text='Address: ')
        lbl_color.place(x=350, y=90)
        self.txt_address = tk.Entry(self.client_details, width=18)
        self.txt_address.place(x=450, y=90)

        # Email
        lbl_email = tk.Label(self.client_details, bg='#484b4c', fg="white", text='Email: ')
        lbl_email.place(x=20, y=120)
        self.txt_email = tk.Entry(self.client_details, width=20)
        self.txt_email.place(x=120, y=120)

        # Gender
        lbl_gender = tk.Label(self.client_details, bg='#484b4c', fg="white", text='Gender: ')
        lbl_gender.place(x=350, y=120)
        self.txt_gender = ttk.Combobox(self.client_details, width=18,
                                     values=["Female", "Male", "Other"], state='readonly')
        self.txt_gender.place(x=450, y=120)

        # Birthday
        lbl_birthday = tk.Label(self.client_details, bg='#484b4c', fg="white", text='Birthday: ')
        lbl_birthday.place(x=350, y=120)
        self.txt_bday = DateEntry(self.client_details, width=20,  background='#4595BE', foreground='white', borderwidth=2,
                          date_pattern='dd/mm/yyyy')
        self.txt_bday.place(x=450, y=120)

        # Edit Button
        self.btn_edit_client = tk.Button(self.client_details, text="Edit Client", width=15, command=self.confirm_edit_client)
        self.btn_edit_client.place(x=600, y=250)

        self.new_frame.place(x=0, y=0)

    def show_edit_details(self):
        if self.txt_select_client.get() != "":
            self.client_details.place(x=10, y=130)
            df_client = self.data.get_client_data_by_id(self.txt_select_client.get())
            self.txt_id.config(state='normal')
            self.txt_id.delete(0, tk.END)
            self.txt_id.insert(0, df_client['ID'].iloc[0])
            self.txt_id.config(state='readonly')
            self.txt_name.delete(0, tk.END)
            self.txt_name.insert(0, df_client['Name'].iloc[0])
            self.txt_last_name.delete(0, tk.END)
            self.txt_last_name.insert(0, df_client['Last Name'].iloc[0])
            self.txt_phone_number.delete(0, tk.END)
            self.txt_phone_number.insert(0, df_client['Phone Number'].iloc[0])
            self.txt_address.delete(0, tk.END)
            self.txt_address.insert(0, df_client['Address'].iloc[0])
            self.txt_email.delete(0, tk.END)
            self.txt_email.insert(0, df_client['Email'].iloc[0])
            self.txt_gender.set(df_client['Gender'].iloc[0])
            self.txt_bday.delete(0, tk.END)
            self.txt_bday.insert(0, df_client['Birthday'].iloc[0])
        else:
            messagebox.showerror("Error!!!", "No se ha seleccionado ningun ID")

    def confirm_edit_client(self):
        answer = messagebox.askyesno("Confirmar edicion", "Desea editar el cliente? ")
        if answer:
            if (self.validate_client_info()):
                client_dict = {
                    'ID': self.txt_id.get(),
                    'Name': self.txt_name.get(),
                    'Last Name': self.txt_last_name.get(),
                    'Phone number': self.txt_phone_number.get(),
                    'Address': self.txt_address.get(),
                    'Email': self.txt_email.get(),
                    'Gender': self.txt_gender.get(),
                    'Birthday': self.txt_bday.get(),
                }
                self.data.edit_client(client_dict)
                messagebox.showinfo("Se edito con exito!", "El cliente se ha editado con exito!!!")
            else:
                messagebox.showinfo("Mal!", "Algo anda mal")
        else:
            messagebox.showinfo("Sin cambios", "No se realizo ningun cambio.")


