import data
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re

class Car_interface:
    def __init__(self, Data, content_frame, bottom_frame):
        self.data = Data
        self.content_frame = content_frame
        self.bottom_frame = bottom_frame
        self.content_frame.update_idletasks()  # Asegura que el layout esté calculado
        self.bottom_frame.update_idletasks()  # Asegura que el layout esté calculado
        self.models = {'Mercedez-Benz' : ['Clase C Sedán', 'CLA Coupé'],
                       'Audi' : ['A1', 'A2', 'A3'],
                       'BMW' : ['Serie 1', 'Serie 2', 'Serie 3'],
                       'Acura' : ['ITEGRA', 'TLX'],
                       'GMC' : ['Denali', 'Terrain'],
                       'Maserati' : ['Grecale', 'MODENA'],
                       'Lexus' : ['IS', 'ES', 'LS']
                       }

    def update_models(self, event):
        brand = self.txt_brand.get()
        models = self.models.get(brand, [])
        self.txt_model.set('') # clean field
        self.txt_model['values'] = models

    def new_car(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="New Car",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # Id
        lbl_id = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Entry(self.new_label_frame, width=20)
        self.txt_id.insert(0, str(self.data.get_next_car_id()))
        self.txt_id.config(state='readonly')
        self.txt_id.place(x=120, y=20)

        # Brand
        lbl_brand = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Brand: ')
        lbl_brand.place(x=20, y=60)
        self.txt_brand = ttk.Combobox(self.new_label_frame, width=18, state="readonly", values=list(self.models.keys()))
        self.txt_brand.place(x=120, y=60)

        self.txt_brand.bind('<<ComboboxSelected>>', self.update_models) # bind update_models() to combo brand event

        # Model
        lbl_model = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Model: ')
        lbl_model.place(x=350, y=60)
        self.txt_model = ttk.Combobox(self.new_label_frame, width=18, state="readonly")
        self.txt_model.place(x=450, y=60)

        # Transmission
        lbl_transmission = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Transmission: ')
        lbl_transmission.place(x=20, y=90)
        self.txt_transmission = ttk.Combobox(self.new_label_frame, values=['Manual', 'Automatic'],
                                             state="readonly", width=18)
        self.txt_transmission.place(x=120, y=90)

        # Color
        lbl_color = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Color: ')
        lbl_color.place(x=350, y=90)
        self.txt_color = ttk.Combobox(self.new_label_frame, width=18, values=['Red', 'White', 'Black', 'Blue', 'Grey'],
                                      state="readonly")
        self.txt_color.place(x=450, y=90)

        # Price
        lbl_price = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Price: ')
        lbl_price.place(x=20, y=120)
        self.txt_price = tk.Entry(self.new_label_frame, width=20)
        self.txt_price.place(x=120, y=120)

        # Year
        lbl_year = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Year: ')
        lbl_year.place(x=350, y=120)
        self.txt_year = ttk.Combobox(self.new_label_frame, width=18, values=['2020', '2021', '2022', '2023', '2024', '2025'],
                                     state="readonly")
        self.txt_year.place(x=450, y=120)

        # Km
        lbl_km = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Km: ')
        lbl_km.place(x=20, y=150)
        self.txt_km = tk.Entry(self.new_label_frame, width=20)
        self.txt_km.place(x=120, y=150)

        # Car Type
        lbl_car_type = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Car type: ')
        lbl_car_type.place(x=350, y=150)
        self.txt_car_type = ttk.Combobox(self.new_label_frame, width=18, values=['Sedan', 'SUV', 'Coupe', 'Sport'],
                                         state="readonly")
        self.txt_car_type.place(x=450, y=150)

        # Fuel
        lbl_fuel = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Fuel: ')
        lbl_fuel.place(x=20, y=180)
        self.txt_car_fuel = ttk.Combobox(self.new_label_frame, width=18, values=['Gas', 'Electric', 'Hybrid', 'Diesel'],
                                         state="readonly")
        self.txt_car_fuel.place(x=120, y=180)

        # Stock
        lbl_stock = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Stock: ')
        lbl_stock.place(x=350, y=180)
        self.txt_stock = tk.Entry(self.new_label_frame, width=20)
        self.txt_stock.place(x=450, y=180)

        # Buttons
        self.btn_add_car = tk.Button(self.new_label_frame, text="Add Car", width=18, command=self.add_new_car)
        self.btn_add_car.place(x=450, y=280)

        # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock)
        self.new_frame.place(x=0, y=0)

    def delete_car(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="Delete Car",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # select car
        lbl_select_car = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Select car: ')
        lbl_select_car.place(x=20, y=60)
        self.txt_select_car = ttk.Combobox(self.new_label_frame, width=18, state="readonly",
                                           values=self.data.df_cars["ID"].tolist())
        self.txt_select_car.place(x=120, y=60)

        # Buttons
        self.btn_select_car = tk.Button(self.new_label_frame, text="Select Car", width=15,
                                        command=self.show_delete_details)
        self.btn_select_car.place(x=300, y=60)

        # Separator
        separator = tk.Frame(self.new_label_frame, bg='white', height=2, width=self.content_frame.winfo_width() -30)
        separator.place(x=10, y=120)
        self.car_details = tk.Frame(self.new_label_frame, bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 30,
                                             height = self.content_frame.winfo_height() - 180)
        # Car details
        lbl_id = tk.Label(self.car_details, text="ID: ", bg='#484b4c', fg='white')
        lbl_id.place(x=20, y=10)
        self.lbl_id = tk.Label(self.car_details, text="12345", bg='#484b4c', fg="white")
        self.lbl_id.place(x=120, y=10)

        lbl_brand = tk.Label(self.car_details, text="Brand: ", bg='#484b4c', fg='white')
        lbl_brand.place(x=20, y=30)
        self.lbl_brand = tk.Label(self.car_details, text="BMW", bg='#484b4c', fg='white')
        self.lbl_brand.place(x=120, y=30)

        lbl_model = tk.Label(self.car_details, text="Model: ", bg='#484b4c', fg='white')
        lbl_model.place(x=20, y=50)
        self.lbl_model = tk.Label(self.car_details, text="2000", bg='#484b4c', fg='white')
        self.lbl_model.place(x=120, y=50)

        lbl_transmission = tk.Label(self.car_details, text="Transsmision: ", bg='#484b4c', fg='white')
        lbl_transmission.place(x=20, y=70)
        self.lbl_transmission = tk.Label(self.car_details, text="Manual", bg='#484b4c', fg='white')
        self.lbl_transmission.place(x=120, y=70)

        lbl_color = tk.Label(self.car_details, text="Color: ", bg='#484b4c', fg='white')
        lbl_color.place(x=20, y=90)
        self.lbl_color = tk.Label(self.car_details, text="BMW", bg='#484b4c', fg='white')
        self.lbl_color.place(x=120, y=90)

        lbl_price = tk.Label(self.car_details, text="Price: ", bg='#484b4c', fg='white')
        lbl_price.place(x=20, y=110)
        self.lbl_price = tk.Label(self.car_details, text="BMW", bg='#484b4c', fg='white')
        self.lbl_price.place(x=120, y=110)

        lbl_year = tk.Label(self.car_details, text="Year: ", bg='#484b4c', fg='white')
        lbl_year.place(x=20, y=130)
        self.lbl_year = tk.Label(self.car_details, text="BMW", bg='#484b4c', fg='white')
        self.lbl_year.place(x=120, y=130)

        lbl_km = tk.Label(self.car_details, text="Km: ", bg='#484b4c', fg='white')
        lbl_km.place(x=20, y=150)
        self.lbl_km = tk.Label(self.car_details, text="1200", bg='#484b4c', fg='white')
        self.lbl_km.place(x=120, y=150)

        lbl_car_type = tk.Label(self.car_details, text="Car type: ", bg='#484b4c', fg='white')
        lbl_car_type.place(x=20, y=170)
        self.lbl_car_type = tk.Label(self.car_details, text="1200", bg='#484b4c', fg='white')
        self.lbl_car_type.place(x=120, y=170)

        lbl_fuel = tk.Label(self.car_details, text="Fuel: ", bg='#484b4c', fg='white')
        lbl_fuel.place(x=20, y=190)
        self.lbl_fuel = tk.Label(self.car_details, text="1200", bg='#484b4c', fg='white')
        self.lbl_fuel.place(x=120, y=190)

        lbl_stock = tk.Label(self.car_details, text="Stock: ", bg='#484b4c', fg='white')
        lbl_stock.place(x=20, y=210)
        self.lbl_stock = tk.Label(self.car_details, text="1200", bg='#484b4c', fg='white')
        self.lbl_stock.place(x=120, y=210)

        # Delete Button
        self.btn_delete_car = tk.Button(self.car_details, text="Delete Car", width=15, command=self.confirm_delete_car)
        self.btn_delete_car.place(x=600, y=250)

        # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock)
        self.new_frame.place(x=0, y=0)

    def confirm_delete_car(self):
        answer = messagebox.askyesno("Confirmar borrado", "Desea borrar el carro? "
                                                          "(esta opcion no se puede deshacer)")
        if answer:
            self.data.delete_car_by_id(self.txt_select_car.get())
            self.txt_select_car["values"] = values=self.data.df_cars["ID"].tolist()
            if len(values) > 0:
                self.txt_select_car.current(0)
            else:
                self.txt_select_car.set("")
            self.car_details.place_forget()
            messagebox.showinfo("Borrado exitoso!", "El carro se ha eliminado con exito!!!")
        else:
            messagebox.showinfo("Sin cambios", "No se realizo ningun cambio.")

    def show_delete_details(self):
        if self.txt_select_car.get() != "":
            self.car_details.place(x=10, y=130)  # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
            df_car = self.data.get_car_data_by_id(self.txt_select_car.get())
            self.lbl_id.config(text= df_car['ID'].iloc[0])
            self.lbl_brand.config(text=df_car['Brand'].iloc[0])
            self.lbl_model.config(text=df_car['Model'].iloc[0])
            self.lbl_transmission.config(text=df_car['Transmission'].iloc[0])
            self.lbl_color.config(text=df_car['Color'].iloc[0])
            self.lbl_price.config(text=df_car['Price'].iloc[0])
            self.lbl_year.config(text=df_car['Year'].iloc[0])
            self.lbl_km.config(text=df_car['Km'].iloc[0])
            self.lbl_car_type.config(text=df_car['Car Type'].iloc[0])
            self.lbl_fuel.config(text=df_car['Fuel'].iloc[0])
            self.lbl_stock.config(text=df_car['Stock'].iloc[0])
        else:
            messagebox.showerror("Error!!!", "No se ha seleccionado ningun ID")

    def add_new_car(self): #  brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
        if (self.validate_car_info()):
            car_dict = {
                'ID': self.txt_id.get(),
                'Brand': self.txt_brand.get(),
                'Model': self.txt_model.get(),
                'Transmission': self.txt_transmission.get(),
                'Color': self.txt_color.get(),
                'Price': self.txt_price.get(),
                'Year': self.txt_year.get(),
                'Km': self.txt_km.get(),
                'Car Type':self.txt_car_type.get(),
                'Fuel': self.txt_car_fuel.get(),
                'Stock': self.txt_stock.get()
            }
            self.data.add_car(car_dict)
            messagebox.showinfo("Exito!", "EL nuevo carro se ha añadido!")
            self.clear_fields()
        else:
            messagebox.showinfo("Mal!", "Algo anda mal")

    def validate_car_info(self):
        # no validar, precio, km, stock, y id
        regex = r"[+-]?[0-9]+\.[0-9]+"
        if (self.txt_brand.get() == "" or self.txt_model.get() == "" or self.txt_transmission.get() == ""
                or self.txt_color.get() == "" or self.txt_year.get() == "" or self.txt_car_type.get() == ""
                or self.txt_car_fuel.get() == "" or self.txt_price.get() == "" or self.txt_km.get() == ""
                or self.txt_stock.get() == "" or self.txt_id.get() == ""):
            messagebox.showerror("ERROR!!!", "Los campos no pueden estar vacios!")
            return False
        # elif (not self.txt_km.get().isnumeric() or not self.txt_stock.get().isnumeric() or not self.txt_id.get().isnumeric()):
        elif (not (self.txt_km.get().isnumeric() and self.txt_stock.get().isnumeric() and self.txt_id.get().isnumeric())):
            messagebox.showerror("ERROR!!!", "Los campos de km, stock & id deben ser numeros enteros")
            return False
        elif (not re.search(regex, self.txt_price.get())):
            messagebox.showerror("ERROR!!!", "El campo de precio debe ser un numero decimal")
            return False
        else:
            return True

    def clear_fields(self):
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.insert(0, str(self.data.get_next_car_id()))
        self.txt_id.config(state='readonly')
        self.txt_model.set('')
        self.txt_brand.set('')
        self.txt_transmission.set('')
        self.txt_color.set('')
        self.txt_year.set('')
        self.txt_car_type.set('')
        self.txt_car_fuel.set('')

        self.txt_price.delete(0, tk.END)
        self.txt_km.delete(0, tk.END)
        self.txt_stock.delete(0, tk.END)

    def edit_car(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height=self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="Edit Car",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height=self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # select car
        lbl_select_car = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Select car: ')
        lbl_select_car.place(x=20, y=60)
        self.txt_select_car = ttk.Combobox(self.new_label_frame, width=18, state="readonly",
                                           values=self.data.df_cars["ID"].tolist())
        self.txt_select_car.place(x=120, y=60)

        # Buttons
        self.btn_select_car = tk.Button(self.new_label_frame, text="Select Car", width=15,
                                        command=self.show_edit_details)
        self.btn_select_car.place(x=300, y=60)

        # Separator
        separator = tk.Frame(self.new_label_frame, bg='white', height=2, width=self.content_frame.winfo_width() - 30)
        separator.place(x=10, y=120)
        self.car_details = tk.Frame(self.new_label_frame, bg='#484b4c',
                                    width=self.content_frame.winfo_width() - 30,
                                    height=self.content_frame.winfo_height() - 180)
        # Car details
        # Id
        lbl_id = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Entry(self.car_details, width=20)
        self.txt_id.insert(0, str(self.data.get_next_car_id()))
        self.txt_id.config(state='readonly')
        self.txt_id.place(x=120, y=20)

        # Brand
        lbl_brand = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Brand: ')
        lbl_brand.place(x=20, y=60)
        self.txt_brand = ttk.Combobox(self.car_details, width=18, state="readonly", values=list(self.models.keys()))
        self.txt_brand.place(x=120, y=60)

        self.txt_brand.bind('<<ComboboxSelected>>', self.update_models)  # bind update_models() to combo brand event

        # Model
        lbl_model = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Model: ')
        lbl_model.place(x=350, y=60)
        self.txt_model = ttk.Combobox(self.car_details, width=18, state="readonly")
        self.txt_model.place(x=450, y=60)

        # Transmission
        lbl_transmission = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Transmission: ')
        lbl_transmission.place(x=20, y=90)
        self.txt_transmission = ttk.Combobox(self.car_details, values=['Manual', 'Automatic'],
                                             state="readonly", width=18)
        self.txt_transmission.place(x=120, y=90)

        # Color
        lbl_color = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Color: ')
        lbl_color.place(x=350, y=90)
        self.txt_color = ttk.Combobox(self.car_details, width=18, values=['Red', 'White', 'Black', 'Blue', 'Grey'],
                                      state="readonly")
        self.txt_color.place(x=450, y=90)

        # Price
        lbl_price = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Price: ')
        lbl_price.place(x=20, y=120)
        self.txt_price = tk.Entry(self.car_details, width=20)
        self.txt_price.place(x=120, y=120)

        # Year
        lbl_year = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Year: ')
        lbl_year.place(x=350, y=120)
        self.txt_year = ttk.Combobox(self.car_details, width=18,
                                     values=['2020', '2021', '2022', '2023', '2024', '2025'],
                                     state="readonly")
        self.txt_year.place(x=450, y=120)

        # Km
        lbl_km = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Km: ')
        lbl_km.place(x=20, y=150)
        self.txt_km = tk.Entry(self.car_details, width=20)
        self.txt_km.place(x=120, y=150)

        # Car Type
        lbl_car_type = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Car type: ')
        lbl_car_type.place(x=350, y=150)
        self.txt_car_type = ttk.Combobox(self.car_details, width=18, values=['Sedan', 'SUV', 'Coupe', 'Sport'],
                                         state="readonly")
        self.txt_car_type.place(x=450, y=150)

        # Fuel
        lbl_fuel = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Fuel: ')
        lbl_fuel.place(x=20, y=180)
        self.txt_car_fuel = ttk.Combobox(self.car_details, width=18, values=['Gas', 'Electric', 'Hybrid', 'Diesel'],
                                         state="readonly")
        self.txt_car_fuel.place(x=120, y=180)

        # Stock
        lbl_stock = tk.Label(self.car_details, bg='#484b4c', fg="white", text='Stock: ')
        lbl_stock.place(x=350, y=180)
        self.txt_stock = tk.Entry(self.car_details, width=20)
        self.txt_stock.place(x=450, y=180)

        # Delete Button
        self.btn_edit_car = tk.Button(self.car_details, text="Edit Car", width=15, command=self.confirm_edit_car)
        self.btn_edit_car.place(x=600, y=250)

        # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock)
        self.new_frame.place(x=0, y=0)

    def show_edit_details(self):
        if self.txt_select_car.get() != "":
            self.car_details.place(x=10, y=130)  # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
            df_car = self.data.get_car_data_by_id(self.txt_select_car.get())
            self.txt_id.config(state='normal')
            self.txt_id.delete(0, tk.END)
            self.txt_id.insert(0, df_car['ID'].iloc[0])
            self.txt_id.config(state='readonly')
            self.txt_brand.set(df_car['Brand'].iloc[0])
            self.txt_model.set(df_car['Model'].iloc[0])
            self.txt_transmission.set(df_car['Transmission'].iloc[0])
            self.txt_color.set(df_car['Color'].iloc[0])
            self.txt_price.delete(0, tk.END)
            self.txt_price.insert(0, df_car['Price'].iloc[0])
            self.txt_year.set(df_car['Year'].iloc[0])
            self.txt_km.delete(0, tk.END)
            self.txt_km.insert(0, df_car['Km'].iloc[0])
            self.txt_car_type.set(df_car['Car Type'].iloc[0])
            self.txt_car_fuel.set(df_car['Fuel'].iloc[0])
            self.txt_stock.delete(0, tk.END)
            self.txt_stock.insert(0, df_car['Stock'].iloc[0])
        else:
            messagebox.showerror("Error!!!", "No se ha seleccionado ningun ID")

    def confirm_edit_car(self):
        answer = messagebox.askyesno("Confirmar edicion", "Desea editar el carro? ")
        if answer:
            if (self.validate_car_info()):
                car_dict = {
                    'ID': self.txt_id.get(),
                    'Brand': self.txt_brand.get(),
                    'Model': self.txt_model.get(),
                    'Transmission': self.txt_transmission.get(),
                    'Color': self.txt_color.get(),
                    'Price': self.txt_price.get(),
                    'Year': self.txt_year.get(),
                    'Km': self.txt_km.get(),
                    'Car Type': self.txt_car_type.get(),
                    'Fuel': self.txt_car_fuel.get(),
                    'Stock': self.txt_stock.get()
                }
                self.data.edit_car(car_dict)
                messagebox.showinfo("Se edito con exito!", "El carro se ha editado con exito!!!")
            else:
                messagebox.showinfo("Mal!", "Algo anda mal")
        else:
            messagebox.showinfo("Sin cambios", "No se realizo ningun cambio.")
