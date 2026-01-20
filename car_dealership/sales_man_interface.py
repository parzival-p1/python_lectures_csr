import re

import pandas as pd

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
        self.dict_filter = {}
        self.filtered_df = self.data.df_salesmen
        self.table = None

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

        # Gender
        lbl_gender = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Gender: ')
        lbl_gender.place(x=20, y=150)
        self.txt_gender = ttk.Combobox(self.new_label_frame, width=20, values=["Female", "Male", "Other"], state='readonly')
        self.txt_gender.place(x=120, y=150)

        # Buttons
        self.btn_add_employee = tk.Button(self.new_label_frame, text="Add Employee", width=18, command=self.add_new_salesman)
        self.btn_add_employee.place(x=450, y=280)
        self.new_frame.place(x=0, y=0)

    def add_new_salesman(self):  # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
        if (self.validate_salesman_info()):
            salesman_dict = {
                'ID': self.txt_id.get(),
                'Name': self.txt_name.get(),
                'Last Name': self.txt_last_name.get(),
                'Phone Number': self.txt_phone_number.get(),
                'Address': self.txt_address.get(),
                'Email': self.txt_email.get(),
                'Gender': self.txt_gender.get(),
                'Birthday': self.txt_bday.get()
            }
            self.data.add_salesman(salesman_dict)
            messagebox.showinfo("Exito!", "El nuevo empleado se ha añadido!")
            self.clear_fields()
        else:
            messagebox.showinfo("Mal!", "Algo anda mal")

    def validate_salesman_info(self):
        # no validar, precio, km, stock, y id
        regex = r"[+-]?[0-9]+\.[0-9]+"
        if (self.txt_name.get() == "" or self.txt_last_name.get() == "" or self.txt_email.get() == ""
                or self.txt_phone_number.get() == "" or self.txt_address.get() == "" or self.txt_bday.get() == ""
                or self.txt_gender.get() == "" or self.txt_id.get() == ""):
            messagebox.showerror("ERROR!!!", "Los campos no pueden estar vacios!")
            return False

        if not self.validate_email(self.txt_email.get()):
            messagebox.showerror("ERROR!!!", "El mail no tiene formato valido")
            return False
        return True

    def validate_email(self, email: str) -> bool:
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None

    def clear_fields(self):
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

    def delete_salesman(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="Delete Employee",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # select employee
        lbl_select_employee = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Select employee: ')
        lbl_select_employee.place(x=20, y=60)
        self.txt_select_employee = ttk.Combobox(self.new_label_frame, width=18, state="readonly",
                                           values=self.data.df_salesmen["ID"].tolist())
        self.txt_select_employee.place(x=120, y=60)

        # Buttons
        self.btn_select_salesman = tk.Button(self.new_label_frame, text="Select Employee", width=15,
                                        command=self.show_delete_details)
        self.btn_select_salesman.place(x=300, y=60)

        # Separator
        separator = tk.Frame(self.new_label_frame, bg='white', height=2, width=self.content_frame.winfo_width() -30)
        separator.place(x=10, y=120)
        self.salesman_details = tk.Frame(self.new_label_frame, bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 30,
                                             height = self.content_frame.winfo_height() - 180)

        # Salesman details
        lbl_id = tk.Label(self.salesman_details, text="ID: ", bg='#484b4c', fg='white')
        lbl_id.place(x=20, y=10)
        self.lbl_id = tk.Label(self.salesman_details, text="12345", bg='#484b4c', fg="white")
        self.lbl_id.place(x=120, y=10)

        lbl_name = tk.Label(self.salesman_details, text="Name: ", bg='#484b4c', fg='white')
        lbl_name.place(x=20, y=30)
        self.lbl_name = tk.Label(self.salesman_details, text="Name", bg='#484b4c', fg='white')
        self.lbl_name.place(x=120, y=30)

        lbl_last_name = tk.Label(self.salesman_details, text="Last name: ", bg='#484b4c', fg='white')
        lbl_last_name.place(x=20, y=50)
        self.lbl_last_name = tk.Label(self.salesman_details, text="2000", bg='#484b4c', fg='white')
        self.lbl_last_name.place(x=120, y=50)

        lbl_phone_number = tk.Label(self.salesman_details, text="Phone Number: ", bg='#484b4c', fg='white')
        lbl_phone_number.place(x=20, y=70)
        self.lbl_phone_number = tk.Label(self.salesman_details, text="Phone Number", bg='#484b4c', fg='white')
        self.lbl_phone_number.place(x=120, y=70)

        lbl_address = tk.Label(self.salesman_details, text="Address: ", bg='#484b4c', fg='white')
        lbl_address.place(x=20, y=90)
        self.lbl_address = tk.Label(self.salesman_details, text="Address", bg='#484b4c', fg='white')
        self.lbl_address.place(x=120, y=90)

        lbl_email = tk.Label(self.salesman_details, text="Email: ", bg='#484b4c', fg='white')
        lbl_email.place(x=20, y=110)
        self.lbl_email = tk.Label(self.salesman_details, text="Email", bg='#484b4c', fg='white')
        self.lbl_email.place(x=120, y=110)

        lbl_gender = tk.Label(self.salesman_details, text="Gender: ", bg='#484b4c', fg='white')
        lbl_gender.place(x=20, y=130)
        self.lbl_gender = tk.Label(self.salesman_details, text="Gender", bg='#484b4c', fg='white')
        self.lbl_gender.place(x=120, y=130)

        lbl_birthday = tk.Label(self.salesman_details, text="Birthday: ", bg='#484b4c', fg='white')
        lbl_birthday.place(x=20, y=150)
        self.lbl_birthday = tk.Label(self.salesman_details, text="Birthday", bg='#484b4c', fg='white')
        self.lbl_birthday.place(x=120, y=150)

        # Delete Button
        self.btn_delete_salesman = tk.Button(self.salesman_details, text="Delete Salesman", width=15,
                                           command=self.confirm_delete_salesman)
        self.btn_delete_salesman.place(x=600, y=250)

        self.new_frame.place(x=0, y=0)

    def show_delete_details(self):
        if self.txt_select_employee.get() != "":
            self.salesman_details.place(x=10,
                                      y=130)  # 'ID', 'Name', 'Last Name', 'Phone Number', 'Address', 'Email', 'Gender', 'Birthday'
            df_salesman = self.data.get_salesman_data_by_id(self.txt_select_employee.get())
            self.lbl_id.config(text=df_salesman['ID'].iloc[0])
            self.lbl_name.config(text=df_salesman['Name'].iloc[0])
            self.lbl_last_name.config(text=df_salesman['Last Name'].iloc[0])
            self.lbl_phone_number.config(text=df_salesman['Phone Number'].iloc[0])
            self.lbl_address.config(text=df_salesman['Address'].iloc[0])
            self.lbl_email.config(text=df_salesman['Email'].iloc[0])
            self.lbl_gender.config(text=df_salesman['Gender'].iloc[0])
            self.lbl_birthday.config(text=df_salesman['Birthday'].iloc[0])
        else:
            messagebox.showerror("Error!!!", "No se ha seleccionado ningun Empleado")

    def confirm_delete_salesman(self):
        answer = messagebox.askyesno("Confirmar borrado", "Desea borrar el empleado? "
                                                          "(esta opcion no se puede deshacer)")
        if answer:
            self.data.delete_salesman_by_id(self.txt_select_employee.get())
            self.txt_select_employee["values"] = values=self.data.df_salesmen["ID"].tolist()
            if len(values) > 0:
                self.txt_select_employee.current(0)
            else:
                self.txt_select_employee.set("")
            self.salesman_details.place_forget()
            messagebox.showinfo("Borrado exitoso!", "El empleado se ha eliminado con exito!!!")
        else:
            messagebox.showinfo("Sin cambios", "No se realizo ningun cambio.")

    def edit_salesman(self): # 'ID', 'Name', 'Last Name', 'Phone Number', 'Address', 'Email', 'Gender', 'Birthday
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height=self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="Edit Car",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height=self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # select salesman
        lbl_select_salesman = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Select salesman: ')
        lbl_select_salesman.place(x=20, y=60)
        self.txt_select_salesman = ttk.Combobox(self.new_label_frame, width=18, state="readonly",
                                           values=self.data.df_salesmen["ID"].tolist())
        self.txt_select_salesman.place(x=120, y=60)

        # Buttons
        self.btn_select_salesman = tk.Button(self.new_label_frame, text="Select Salesman", width=15,
                                        command=self.show_edit_details)
        self.btn_select_salesman.place(x=300, y=60)

        # Separator
        separator = tk.Frame(self.new_label_frame, bg='white', height=2, width=self.content_frame.winfo_width() - 30)
        separator.place(x=10, y=120)
        self.salesman_details = tk.Frame(self.new_label_frame, bg='#484b4c',
                                    width=self.content_frame.winfo_width() - 30,
                                    height=self.content_frame.winfo_height() - 180)
        # Salesman details
        # Id
        lbl_id = tk.Label(self.salesman_details, bg='#484b4c', fg="white", text='Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Entry(self.salesman_details, width=20)
        self.txt_id.insert(0, str(self.data.get_next_salesman_id()))
        self.txt_id.config(state='readonly')
        self.txt_id.place(x=120, y=20)

        # Name
        lbl_name = tk.Label(self.salesman_details, bg='#484b4c', fg="white", text='Name: ')
        lbl_name.place(x=20, y=60)
        self.txt_name = tk.Entry(self.salesman_details, width=18)
        self.txt_name.place(x=120, y=60)

        # Last name
        lbl_last_name = tk.Label(self.salesman_details, bg='#484b4c', fg="white", text='Last name: ')
        lbl_last_name.place(x=350, y=60)
        self.txt_last_name = tk.Entry(self.salesman_details, width=18)
        self.txt_last_name.place(x=450, y=60)

        # Phone number
        lbl_phone_number = tk.Label(self.salesman_details, bg='#484b4c', fg="white", text='Phone number: ')
        lbl_phone_number.place(x=20, y=90)
        self.txt_phone_number = tk.Entry(self.salesman_details, width=18)
        self.txt_phone_number.place(x=120, y=90)

        # Address
        lbl_color = tk.Label(self.salesman_details, bg='#484b4c', fg="white", text='Address: ')
        lbl_color.place(x=350, y=90)
        self.txt_address = tk.Entry(self.salesman_details, width=18)
        self.txt_address.place(x=450, y=90)

        # Email
        lbl_email = tk.Label(self.salesman_details, bg='#484b4c', fg="white", text='Email: ')
        lbl_email.place(x=20, y=120)
        self.txt_email = tk.Entry(self.salesman_details, width=20)
        self.txt_email.place(x=120, y=120)

        # Gender
        lbl_gender = tk.Label(self.salesman_details, bg='#484b4c', fg="white", text='Gender: ')
        lbl_gender.place(x=350, y=120)
        self.txt_gender = ttk.Combobox(self.salesman_details, width=18,
                                     values=["Female", "Male", "Other"], state='readonly')
        self.txt_gender.place(x=450, y=120)

        # Birthday
        lbl_birthday = tk.Label(self.salesman_details, bg='#484b4c', fg="white", text='Birthday: ')
        lbl_birthday.place(x=350, y=120)
        self.txt_bday = DateEntry(self.salesman_details, width=20,  background='#4595BE', foreground='white', borderwidth=2,
                          date_pattern='dd/mm/yyyy')
        self.txt_bday.place(x=450, y=120)

        # Edit Button
        self.btn_edit_salesman = tk.Button(self.salesman_details, text="Edit Employee", width=15, command=self.confirm_edit_salesman)
        self.btn_edit_salesman.place(x=600, y=250)

        self.new_frame.place(x=0, y=0)

    def show_edit_details(self):
        if self.txt_select_salesman.get() != "":
            self.salesman_details.place(x=10, y=130)
            df_salesman = self.data.get_salesman_data_by_id(self.txt_select_salesman.get())
            self.txt_id.config(state='normal')
            self.txt_id.delete(0, tk.END)
            self.txt_id.insert(0, df_salesman['ID'].iloc[0])
            self.txt_id.config(state='readonly')
            self.txt_name.delete(0, tk.END)
            self.txt_name.insert(0, df_salesman['Name'].iloc[0])
            self.txt_last_name.delete(0, tk.END)
            self.txt_last_name.insert(0, df_salesman['Last Name'].iloc[0])
            self.txt_phone_number.delete(0, tk.END)
            self.txt_phone_number.insert(0, df_salesman['Phone Number'].iloc[0])
            self.txt_address.delete(0, tk.END)
            self.txt_address.insert(0, df_salesman['Address'].iloc[0])
            self.txt_email.delete(0, tk.END)
            self.txt_email.insert(0, df_salesman['Email'].iloc[0])
            self.txt_gender.set(df_salesman['Gender'].iloc[0])
            self.txt_bday.delete(0, tk.END)
            self.txt_bday.insert(0, df_salesman['Birthday'].iloc[0])
        else:
            messagebox.showerror("Error!!!", "No se ha seleccionado ningun ID")

    def confirm_edit_salesman(self):
        answer = messagebox.askyesno("Confirmar edicion", "Desea editar al empleado? ")
        if answer:
            if (self.validate_salesman_info()):
                sales_man_dict = {
                    'ID': self.txt_id.get(),
                    'Name': self.txt_name.get(),
                    'Last Name': self.txt_last_name.get(),
                    'Phone number': self.txt_phone_number.get(),
                    'Address': self.txt_address.get(),
                    'Email': self.txt_email.get(),
                    'Gender': self.txt_gender.get(),
                    'Birthday': self.txt_bday.get(),
                }
                self.data.edit_salesman(sales_man_dict)
                messagebox.showinfo("Se edito con exito!", "El empleado se ha editado con exito!!!")
            else:
                messagebox.showinfo("Mal!", "Algo anda mal")
        else:
            messagebox.showinfo("Sin cambios", "No se realizo ningun cambio.")

# 'Name', 'Last Name', 'Gender'
    def print_all_employees(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="List of Employees",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # Name
        lbl_filter_name = tk.Label(self.new_label_frame, text="Name", background='#484b4c', foreground='white')
        lbl_filter_name.place(x=10, y=40)
        name_list = self.data.df_salesmen['Name'].unique().tolist()
        name_list.append('All')
        self.txt_filter_name = ttk.Combobox(self.new_label_frame, width=10, values=name_list, state="readonly")
        self.txt_filter_name.place(x=10, y=60)
        # lambda event: self.filter_table(event, "mi_parametro")
        self.txt_filter_name.bind("<<ComboboxSelected>>",
                                   lambda event: self.filter_table(event, self.txt_filter_name.get(), "Name"))

        # Last Name
        lbl_filter_last_name = tk.Label(self.new_label_frame, text="Last name", background='#484b4c', foreground='white')
        lbl_filter_last_name.place(x=100, y=40)
        last_name_list = self.data.df_salesmen['Last Name'].unique().tolist()
        last_name_list.append('All')
        self.txt_filter_last_name = ttk.Combobox(self.new_label_frame, width=10, values=last_name_list, state="readonly")
        self.txt_filter_last_name.place(x=100, y=60)
        # lambda event: self.filter_table(event, "mi_parametro")
        self.txt_filter_last_name.bind("<<ComboboxSelected>>",
                                   lambda event: self.filter_table(event, self.txt_filter_last_name.get(), "Last Name"))

        # Gender
        lbl_filter_gender = tk.Label(self.new_label_frame, text="Gender", background='#484b4c', foreground='white')
        lbl_filter_gender.place(x=190, y=40)
        gender_list = self.data.df_salesmen['Gender'].unique().tolist()
        gender_list.append('All')
        self.txt_filter_gender = ttk.Combobox(self.new_label_frame, width=10, values=gender_list, state="readonly")
        self.txt_filter_gender.place(x=190, y=60)
        # lambda event: self.filter_table(event, "mi_parametro")
        self.txt_filter_gender.bind("<<ComboboxSelected>>",
                                   lambda event: self.filter_table(event, self.txt_filter_gender.get(), "Gender"))

        # Birthday
        lbl_filter_bday = tk.Label(self.new_label_frame, text="Birthday", background='#484b4c', foreground='white')
        lbl_filter_bday.place(x=280, y=10)
        # Month
        lbl_filter_month = tk.Label(self.new_label_frame, text="Month", background='#484b4c', foreground='white')
        lbl_filter_month.place(x=280, y=40)
        month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        # month_list = pd.to_datetime(self.data.df_salesmen["Birthday"], format="mixed", dayfirst=True).dt.month_name(locale="es_ES").tolist()
        month_list.append('All')
        self.txt_filter_month = ttk.Combobox(self.new_label_frame, width=10, values=month_list, state="readonly")
        self.txt_filter_month.place(x=280, y=60)
        # lambda event: self.filter_table(event, "mi_parametro")
        self.txt_filter_month.bind("<<ComboboxSelected>>",
                                   lambda event: self.filter_table(event, self.txt_filter_month.get(), "Month"))

        # Year
        lbl_filter_year = tk.Label(self.new_label_frame, text="Year", background='#484b4c', foreground='white')
        lbl_filter_year.place(x=370, y=40)
        year_list = sorted(set(pd.to_datetime(self.data.df_salesmen["Birthday"], format="mixed",
                                   dayfirst=True).dt.year.tolist()))
        year_list.append('All')
        self.txt_filter_year = ttk.Combobox(self.new_label_frame, width=10, values=year_list, state="readonly")
        self.txt_filter_year.place(x=370, y=60)
        # lambda event: self.filter_table(event, "mi_parametro")
        self.txt_filter_year.bind("<<ComboboxSelected>>",
                                   lambda event: self.filter_table(event, self.txt_filter_year.get(), "Year"))

        self.table = ttk.Treeview(self.new_label_frame, columns=('ID', 'Name', 'Last Name', 'Phone Number', 'Address',
                                                                 'Email', 'Gender', 'Birthday'),
                                  show="headings", height=10)
        self.table.place(x=10, y=100)

        # Definir encabezados
        for col in ('ID', 'Name', 'Last Name', 'Phone Number', 'Address', 'Email', 'Gender', 'Birthday'):
            self.table.heading(col, text=col)
            self.table.column(col, anchor="center", width=90)

        self.fill_table()

        self.new_frame.place(x=0, y=0)

    def filter_table(self, event, selected, column):
        if selected == 'All' :
            self.filtered_df = self.data.df_cars
            if column in self.dict_filter:
                del self.dict_filter[column]
            for key, value in self.dict_filter.items():
                self.filtered_df = self.filtered_df[self.filtered_df[key] == value]
        else:
            self.filtered_df = self.filtered_df[self.filtered_df[column] == selected]
            self.dict_filter[column] = selected
        self.fill_table()

    def fill_table(self):
        # Limpiar tabla
        for item in self.table.get_children():
            self.table.delete(item)
        # Insertar filas
        for _, row in self.filtered_df.iterrows():
            self.table.insert("", "end", values=list(row))

"""
    0. Arreglar la interfaz de print all salesmen, filtros y tabla
    1. Agregar la img de whatsapp
    2. Dos filtros extra, mont and year
"""