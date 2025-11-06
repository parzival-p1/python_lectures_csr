import data
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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
        self.btn_add_car = tk.Button(self.new_label_frame, text="Add Car", width=18)
        self.btn_add_car.place(x=450, y=280)

        # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock)
        self.new_frame.place(x=0, y=0)

    def add_new_car(self): #  brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
        pass

    def validate_car_info(self):
        # no validar, precio, km, stock, y id
        if (self.txt_brand.get() == "" or self.txt_model.get() == "" or self.txt_transmission.get() == ""
                or self.txt_color.get() == "" or self.txt_year.get() == "" or self.txt_car_type.get() == ""
                or self.txt_car_fuel.get() == "" or self.txt_price.get() == "", self.txt_km.get() == ""
                or self.txt_stock.get() == "" or self.txt_id.get() == ""):
            return False
        elif (not self.txt_km.get().isnumeric() or not self.txt_stock.get().isnumeric() or not self.txt_id.get().isnumeric()):

        elif (not self.txt_km.get().isnumeric() and not self.txt_stock.get().isnumeric() and not self.txt_id.get().isnumeric()):

            return False

