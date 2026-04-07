from numpy.ma.core import indices

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
        self.item_count = 1
        # Save Data for combo box brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
        self.dict_cars = {row['ID']: [row["Stock"], f"{row['Brand']} {row['Model']} {row["Color"]} {row["Year"]} "
                                                    f"{row["Car Type"]} {row['Transmission']} {row['Km']}Km "
                                                    f"{row['Fuel']}", row['Price']]
                             for _, row in self.data.df_cars.iterrows()}

        self.dict_clients = {row['ID']: f"{row['Name']} {row['Last Name']}"
                             for _, row in self.data.df_clients.iterrows()}

        self.dict_salesmen = {row['ID']: f"{row['Name']} {row['Last Name']}"
                             for _, row in self.data.df_salesmen.iterrows()}

        self.subtotal = 0

    def new_invoice(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height=self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="New Invoice",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height=self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # Id de la factura
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
        self.btn_new_concept.place(x=600, y=65)

        self.invoice_label_frame = tk.LabelFrame(self.new_frame, text="Description",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 40,
                                             height=self.content_frame.winfo_height() - 260,
                                             fg='white')
        self.invoice_label_frame.place(x=10, y=110)

        # subtotal
        lbl_subtotal = tk.Label(self.new_label_frame,  bg='#484b4c', fg="white", text='SUBTOTAL: $')
        lbl_subtotal.place(x=550, y=300)
        self.lbl_subtotal_cur = tk.Label(self.new_label_frame,  bg='#484b4c', fg="white", text='')
        self.lbl_subtotal_cur.place(x=620, y=300)

        # taxes
        lbl_iva = tk.Label(self.new_label_frame,  bg='#484b4c', fg="white", text='IVA: $')
        lbl_iva.place(x=550, y=320)
        self.lbl_iva_cur = tk.Label(self.new_label_frame,  bg='#484b4c', fg="white", text='')
        self.lbl_iva_cur.place(x=620, y=320)

        # total
        lbl_total = tk.Label(self.new_label_frame,  bg='#484b4c', fg="white", text='TOTAL: $')
        lbl_total.place(x=550, y=340)
        self.lbl_total_cur = tk.Label(self.new_label_frame,  bg='#484b4c', fg="white", text='')
        self.lbl_total_cur.place(x=620, y=340)

        # Buttons
        self.btn_print_invoice = tk.Button(self.new_label_frame, text="Print Invoice", width=18, command=self.print_new_invoice)
        self.btn_print_invoice.place(x=450, y=400)
        self.btn_add_invoice = tk.Button(self.new_label_frame, text="Add Invoice", width=18, command=self.add_new_invoice)
        self.btn_add_invoice.place(x=600, y=400)

        self.new_frame.place(x=0, y=0)

    def cancel_invoice(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height=self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="Cancel Invoice",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height=self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)

        # select car
        lbl_select_invoice = tk.Label(self.new_label_frame, bg='#484b4c', fg="white", text='Select Invoice: ')
        lbl_select_invoice.place(x=20, y=60)
        self.txt_select_invoice = ttk.Combobox(self.new_label_frame, width=18, state="readonly",
                                           values=self.data.df_invoices["ID"].tolist())
        self.txt_select_invoice.place(x=120, y=60)

        # Buttons
        self.btn_select_invoice = tk.Button(self.new_label_frame, text="Select Invoice", width=15,
                                        command=self.show_invoice_details)
        self.btn_select_invoice.place(x=300, y=60)

        # Separator
        separator = tk.Frame(self.new_label_frame, bg='white', height=2, width=self.content_frame.winfo_width() - 30)
        separator.place(x=10, y=120)
        self.invoice_details = tk.Frame(self.new_label_frame, bg='#484b4c',
                                    width=self.content_frame.winfo_width() - 30,
                                    height=self.content_frame.winfo_height() - 180)
        # Invoice details
        # ID
        lbl_id = tk.Label(self.invoice_details, bg='#484b4c', fg="white", text='Id: ')
        lbl_id.place(x=20, y=20)
        self.txt_id = tk.Label(self.invoice_details, width=20)
        self.txt_id['text'] = ''
        self.txt_id.place(x=120, y=20)

        # Date
        lbl_date = tk.Label(self.invoice_details, bg='#484b4c', fg="white", text='Date: ')
        lbl_date.place(x=330, y=20)
        self.txt_date = tk.Label(self.invoice_details, width=20)
        self.txt_date['text'] = ''
        self.txt_date .place(x=400, y=20)

        # Client
        lbl_client = tk.Label(self.invoice_details, bg='#484b4c', fg="white", text='Client: ')
        lbl_client.place(x=20, y=50)
        self.txt_client = tk.Label(self.invoice_details, width=20)
        self.txt_client['text'] = ''
        self.txt_client.place(x=120, y=50)

        # Employee ID
        lbl_employee = tk.Label(self.invoice_details, bg='#484b4c', fg="white", text='Employee: ')
        lbl_employee.place(x=330, y=50)
        self.txt_employee = tk.Label(self.invoice_details, width=20)
        self.txt_employee['text'] = ''
        self.txt_employee.place(x=400, y=50)

        # Total
        lbl_total = tk.Label(self.invoice_details, bg='#484b4c', fg="white", text='Total: ')
        lbl_total.place(x=330, y=80)
        self.txt_total = tk.Label(self.invoice_details, width=20)
        self.txt_total['text'] = ''
        self.txt_total.place(x=400, y=80)

        # Cancel Button
        self.btn_edit_invoice = tk.Button(self.invoice_details, text="Cancel Invoice", width=15,
                                          command=self.confirm_cancel_invoice)
        self.btn_edit_invoice.place(x=600, y=250)

        self.new_frame.place(x=0, y=0)

    def confirm_cancel_invoice(self):
        pass

    def show_invoice_details(self):
        if self.txt_select_invoice.get() != "":
            self.invoice_details.place(x=10, y=130)
            df_invoice = self.data.get_invoice_data_by_id(self.txt_select_invoice.get())
            self.txt_id['text'] = df_invoice['ID'].iloc[0]
            self.txt_client['text'] = df_invoice['Client ID'].iloc[0]
            self.txt_employee['text'] = df_invoice['Employee ID'].iloc[0]
            self.txt_date['text'] = df_invoice['Date'].iloc[0]
            self.txt_total['text'] = df_invoice['Total'].iloc[0]
        else:
            messagebox.showerror("Error!!!", "No se ha seleccionado ningun ID")

    def validate_invoice(self):
        if self.txt_client.get() == '':
            messagebox.showerror('Error!', 'Por favor seleccione un cliente...!')
            return False
        elif self.txt_salesman.get() == '':
            messagebox.showerror('Error!', 'Por favor seleccione un vendedor')
            return False
        elif len(self.item_list) < 1:
            messagebox.showerror('Error', 'Agregue al menos un concepto!')
            return False
        else:
            ids = True
            stocks = True

            repeted_items = len(self.item_list) != len(set(self.item_list))
            for item in self.item_list:
                if item.txt_car_id.get() == '':
                    ids = False
                elif item.txt_car_stock.get() == '':
                    stocks = False

            if not ids:
                messagebox.showerror('Error!', 'Seleccione un ID')
                return False
            elif not stocks:
                messagebox.showerror('Error!', 'Seleccione un stock')
                return False
            elif repeted_items:
                messagebox.showerror("Error!", "Los Conceptos no deben repetirse!")
                return False
            else:
                return True

    def update_totals(self):
        self.subtotal = 0
        for item in self.item_list:
            if item.txt_car_stock.get() != "":
                price = float(self.dict_cars[item.txt_car_id.get()][2])
                self.subtotal += int(item.txt_car_stock.get()) * price
        sub =  f"{self.subtotal:.2f}"
        iva = f"{self.subtotal *.16:.2f}"
        total = f"{self.subtotal * 1.16:.2f}"

        self.lbl_subtotal_cur.config(text=sub)
        self.lbl_iva_cur.config(text=iva)
        self.lbl_total_cur.config(text=total)

    def add_new_invoice(self):
        if self.validate_invoice():
            key_client = next((k for k, v in self.dict_clients.items() if v == self.txt_client.get()), None)
            key_salesmen = next((k for k, v in self.dict_salesmen.items() if v == self.txt_salesman.get()), None)

            invoice_dict = {
                'ID': self.txt_id.get(),
                'Client ID': key_client,
                'Employee ID': key_salesmen,
                'Date': self.txt_date.get(),
                'Total': self.lbl_total_cur['text'],
                'Status': "Active"
            }

            self.data.add_invoice(invoice_dict)
            for item in self.item_list:
                sales_dict = {
                    'ID' : self.data.sales_id,
                    'Invoice' : self.txt_id.get(),
                    'Description' : item.txt_car_id.get(),
                    'Quantity' : item.txt_car_stock.get(),
                    'Unit price' : item.lbl_unit_price['text']
                }
                self.data.add_sales(sales_dict)
                stock_total = str(int(self.dict_cars[item.txt_car_id.get()][0]) - int(item.txt_car_stock.get()))
                self.data.df_cars.loc[self.data.df_cars["ID"] == item.txt_car_id.get(), "Stock"] = stock_total
                if stock_total == '0':
                    del self.dict_cars[item.txt_car_id.get()]
                else:
                    self.dict_cars[item.txt_car_id.get()][0] = stock_total
            messagebox.showinfo("Exito!", "La nueva factura se ha añadido!")
            self.clear_fields()

    def print_new_invoice(self):
        pass
    "Como imprimir un pdf? necesito otra librera"

    def clear_fields(self):
        self.txt_id.config(state='normal')
        self.txt_id.delete(0, tk.END)
        self.txt_id.insert(0, str(self.data.get_next_invoice_id()))
        self.txt_id.config(state='readonly')
        self.txt_client.set('')
        self.txt_salesman.set('')

        self.lbl_subtotal_cur['text'] = ''
        self.lbl_total_cur['text'] = ''
        self.lbl_iva_cur['text'] = ''

        while len(self.item_list) > 0:
            self.item_list[0].delete_row()

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
        if self.item_count < 7:
            new_item = invoice_item.Invoice_item(self.invoice_label_frame, self.dict_cars, self, self.item_y)
            self.item_y += 25
            self.item_list.append(new_item)
            new_item.show_row()
            self.item_count += 1
        else:
            messagebox.showinfo("Max concepts reached", "You have reached the max count of concepts!")

    def remove_item(self, item):
        if item in self.item_list:
            self.item_list.remove(item)
            if item.row_frame.winfo_exists():
                item.row_frame.destroy()
                del item
            self.item_count -= 1
            self.item_y -= 25
            # recalcula posiciones desde cero
            for i, it in enumerate(self.item_list):
                it.y = i * 25 + 5  # o el offset inicial que uses
                it.row_frame.place(x=5, y=it.y)
                # print(f"Item {i}: y={it.y}")
            # actualiza item_y al final
            # self.item_y = len(self.item_list) * 25 + 5

"""
TAREA: 
INVESTIGAR:
    0. En la func show_invoice_details(): investigar como poner el nombre en lugar del id 
    sacar de los df de clientes Y empleados.
"""
