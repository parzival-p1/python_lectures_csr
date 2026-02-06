import data
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

import invoice_item


class Invoice_interface:
    def __init__(self, Data, content_frame, bottom_frame):
        self.data = Data
        self.content_frame = content_frame
        self.bottom_frame = bottom_frame
        self.content_frame.update_idletasks()  # Asegura que el layout esté calculado
        self.bottom_frame.update_idletasks()  # Asegura que el layout esté calculado
        self.item_list = []
        self.filtered_df = self.data.df_sales
        self.table = None
        self.dict_filter = {}
        self.item_y = 5
        # Save Data for combo box brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
        self.dict_cars = {row['ID']: [row["Stock"], f"{row['Brand']} {row['Model']} {row["Color"]} {row["Year"]} {row["Car Type"]}"]
                             for _, row in self.data.df_cars.iterrows()}

        self.dict_clients = {row['ID']: f"{row['Name']} {row['Last Name']}"
                             for _, row in self.data.df_clients.iterrows()}

        self.dict_salesmen = {row['ID']: f"{row['Name']} {row['Last Name']}"
                             for _, row in self.data.df_salesmen.iterrows()}

    def new_invoice(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height=self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="New Invoice",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height=self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # Id
        lbl_id = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Entry(self.new_label_frame, width=20)
        self.txt_id.insert(0, str(self.data.get_next_invoice_id()))
        self.txt_id.config(state='readonly')
        self.txt_id.place(x=60, y=20)

        # Date
        lbl_date = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Date: ')
        lbl_date.place(x=340, y=20)
        self.txt_date = DateEntry(self.new_label_frame, width=20,  background='#4595BE', foreground='white',
                                  borderwidth=2, date_pattern='dd/mm/yyyy')
        self.txt_date.place(x=400, y=20)

        # Client
        lbl_client = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Client: ')
        lbl_client.place(x=20, y=50)
        self.txt_client = ttk.Combobox(self.new_label_frame, width=18, state="readonly",
                                       values=list(self.dict_clients.values()))
        self.txt_client.place(x=60, y=50)

        # Salesman
        lbl_salesman = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Salesman: ')
        lbl_salesman.place(x=340, y=50)
        self.txt_salesman = ttk.Combobox(self.new_label_frame, width=20, state="readonly",
                                         values=list(self.dict_salesmen.values()))
        self.txt_salesman.place(x=400, y=50)
        self.btn_new_concept = tk.Button(self.new_label_frame, text="New Concept", width=15, command=self.new_row)
        self.btn_new_concept.place(x=700, y=5)

        self.invoice_label_frame = tk.LabelFrame(self.new_frame, text="Description",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 20,
                                             height=self.content_frame.winfo_height() - 160,
                                             fg='white')
        self.invoice_label_frame.place(x=10, y=110)

        # Buttons
        self.btn_print_invoice = tk.Button(self.new_label_frame, text="Print Invoice", width=18, command=self.print_new_invoice)
        self.btn_print_invoice.place(x=450, y=400)
        self.btn_add_invoice = tk.Button(self.new_label_frame, text="Add Invoice", width=18, command=self.add_new_invoice)
        self.btn_add_invoice.place(x=600, y=400)

        self.new_frame.place(x=0, y=0)

    def add_new_invoice(self):  # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
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
            self.data.add_car(car_dict)
            messagebox.showinfo("Exito!", "EL nuevo carro se ha añadido!")
            self.clear_fields()
        else:
            messagebox.showinfo("Mal!", "Algo anda mal")

    def print_new_invoice(self):
        pass


    def validate_car_info(self):
        pass

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

    def print_all_invoices(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height=self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="List of Cars",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height=self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # brand
        lbl_filter_brand = tk.Label(self.new_label_frame, text="Brand", background='#484b4c', foreground='white')
        lbl_filter_brand.place(x=10, y=10)
        brand_list = self.data.df_cars['Brand'].unique().tolist()
        brand_list.append('All')
        self.txt_filter_brand = ttk.Combobox(self.new_label_frame, width=10, values=brand_list, state="readonly")
        self.txt_filter_brand.place(x=10, y=30)
        # lambda event: self.filter_table(event, "mi_parametro")
        self.txt_filter_brand.bind("<<ComboboxSelected>>",
                                   lambda event: self.filter_table(event, self.txt_filter_brand.get(), "Brand"))

        # model
        lbl_filter_model = tk.Label(self.new_label_frame, text="Model", background='#484b4c', foreground='white')
        lbl_filter_model.place(x=100, y=10)
        model_list = self.data.df_cars['Model'].unique().tolist()
        model_list.append('All')
        self.txt_filter_model = ttk.Combobox(self.new_label_frame, width=10, values=model_list, state="readonly")
        self.txt_filter_model.place(x=100, y=30)
        self.txt_filter_model.bind("<<ComboboxSelected>>",
                                   lambda event: self.filter_table(event, self.txt_filter_model.get(), "Model"))

        # transmission
        lbl_filter_transmission = tk.Label(self.new_label_frame, text="Transmission", background='#484b4c',
                                           foreground='white')
        lbl_filter_transmission.place(x=190, y=10)
        transmission_list = self.data.df_cars["Transmission"].unique().tolist()
        transmission_list.append('All')
        self.txt_filter_transmission = ttk.Combobox(self.new_label_frame, width=10, values=transmission_list,
                                                    state="readonly")
        self.txt_filter_transmission.place(x=190, y=30)
        self.txt_filter_transmission.bind("<<ComboboxSelected>>",
                                          lambda event: self.filter_table(event, self.txt_filter_transmission.get(),
                                                                          "Transmission"))

        # color
        lbl_filter_color = tk.Label(self.new_label_frame, text="Color", background='#484b4c', foreground='white')
        lbl_filter_color.place(x=280, y=10)
        color_list = self.data.df_cars["Color"].unique().tolist()
        color_list.append('All')
        self.txt_filter_color = ttk.Combobox(self.new_label_frame, width=10, values=color_list, state="readonly")
        self.txt_filter_color.place(x=280, y=30)
        self.txt_filter_color.bind("<<ComboboxSelected>>",
                                   lambda event: self.filter_table(event, self.txt_filter_color.get(),
                                                                   "Color"))

        # year
        lbl_filter_year = tk.Label(self.new_label_frame, text="Year", background='#484b4c', foreground='white')
        lbl_filter_year.place(x=370, y=10)
        year_list = self.data.df_cars['Year'].unique().tolist()
        year_list.append('All')
        self.txt_filter_year = ttk.Combobox(self.new_label_frame, width=10, values=year_list, state="readonly")
        self.txt_filter_year.place(x=370, y=30)
        self.txt_filter_year.bind("<<ComboboxSelected>>",
                                  lambda event: self.filter_table(event, self.txt_filter_year.get(), "Year"))

        # car type
        lbl_filter_car_type = tk.Label(self.new_label_frame, text="Car Type", background='#484b4c', foreground='white')
        lbl_filter_car_type.place(x=460, y=10)
        car_type_list = self.data.df_cars["Car Type"].unique().tolist()
        car_type_list.append('All')
        self.txt_filter_car_type = ttk.Combobox(self.new_label_frame, width=10, values=car_type_list, state="readonly")
        self.txt_filter_car_type.place(x=460, y=30)
        self.txt_filter_car_type.bind("<<ComboboxSelected>>",
                                      lambda event: self.filter_table(event, self.txt_filter_car_type.get(),
                                                                      "Car Type"))

        # fuel
        lbl_filter_car_fuel = tk.Label(self.new_label_frame, text="Fuel", background='#484b4c', foreground='white')
        lbl_filter_car_fuel.place(x=550, y=10)
        fuel_list = self.data.df_cars["Fuel"].unique().tolist()
        fuel_list.append('All')
        self.txt_filter_fuel = ttk.Combobox(self.new_label_frame, width=10, values=fuel_list, state="readonly")
        self.txt_filter_fuel.place(x=550, y=30)
        self.txt_filter_fuel.bind("<<ComboboxSelected>>",
                                  lambda event: self.filter_table(event, self.txt_filter_fuel.get(),
                                                                  "Fuel"))
        # table frame
        # Crear Treeview
        self.table = ttk.Treeview(self.new_label_frame, columns=('ID', 'Brand', 'Model', 'Transmission', 'Color', 'Price',
                                                                 'Year', 'Km', 'Car Type',
                                                                 'Fuel', 'Stock'), show="headings")
        self.table.place(x=10, y=60)

        # Definir encabezados
        for col in ('ID', 'Brand', 'Model', 'Transmission', 'Color', 'Price', 'Year', 'Km', 'Car Type', 'Fuel', 'Stock'):
            self.table.heading(col, text=col)
            self.table.column(col, anchor="center", width=60)

        self.fill_table()

        self.new_frame.place(x=0, y=0)

        # Función que se ejecuta al seleccionar un valor

    def filter_table(self, event, selected, column):
        self.filtered_df = self.data.df_cars
        if selected == 'All':
            if column in self.dict_filter:
                del self.dict_filter[column]
        else:
            self.dict_filter[column] = selected
        for key, value in self.dict_filter.items():
            self.filtered_df = self.filtered_df[self.filtered_df[key] == value]

        self.fill_table()

    def fill_table(self):
        # Limpiar tabla
        for item in self.table.get_children():
            self.table.delete(item)
        # Insertar filas
        for _, row in self.filtered_df.iterrows():
            self.table.insert("", "end", values=list(row))

    def new_row(self):
        new_item = invoice_item.Invoice_item(self.invoice_label_frame, self.dict_cars, self, self.item_y)
        self.item_y += 15
        self.item_list.append(new_item)
        new_item.show_row()

    def remove_item(self, item):
        if item in self.item_list:
            self.item_list.remove(item)


"""
    TAREA: INVESTIGAR
        0. Investigar como duplicar la linea de DEscription + New
        1. Una vez duplicada, como le hago para borrar el boton de new de la primer fila (solo debe haber un boton de New)
        2. Como limitar a maximo 5 renglones la descripcion
"""