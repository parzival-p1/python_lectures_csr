import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from data import Data
from PIL import Image, ImageTk
from car_interface import Car_interface
from sales_interface import Sales_interface
from sales_man_interface import Sales_man_interface
from client_interface import Client_interface

class Interface:
    def __init__(self):
        # window
        self.width = 1000
        self.height = 700
        self.window = tk.Tk() # crea obj de tipo Tk (es la ventana)
        self.window.config(width=self.width, height=self.height, bg="#FFFFFF")
        self.window.title("Car Dealership")
        self.window.resizable(width=False, height=False)

        # main frame
        self.main_frame = tk.Frame(self.window, width=self.width, height=self.height, bg='#000000')
        self.main_frame.pack(fill="both", expand=True)

        # top bar
        self.top_bar_frame = tk.Frame(self.main_frame, width=self.width-20, height=self.height/6, bg='#EEEEEE')
        self.top_bar_frame.place(x=10, y=10)

        # left bar
        self.left_bar_frame = tk.Frame(self.main_frame, width=self.width/5, height=self.height - 30 - self.height/6,
                                       bg='#4595BE')
        self.left_bar_frame.place(x=10, y=20 + self.height/6)

        # content frame
        self.content_frame = tk.Frame(self.main_frame, width=self.width - 30 - self.width/5, height=4 * self.height/6,
                                      bg='#484b4c')
        self.content_frame.place(x=20 + self.width/5, y=20 + self.height/6)

        # bottom frame
        self.bottom_frame = tk.Frame(self.main_frame, width=self.width - 30  - self.width/5, height=self.height/10,
                                     bg='#e4e6e8')
        self.bottom_frame.place(x=20 + self.width/5, y=30 + (5 * self.height)/6)

        self.data = Data() # main obj that contains all the info
        self.data.load_data()
        self.data.print_data()
        self.car_interface = Car_interface(self.data, self.content_frame, self.bottom_frame)
        self.sales_man_interface = Sales_man_interface(self.data, self.content_frame, self.bottom_frame)
        self.client_interface = Client_interface(self.data, self.content_frame, self.bottom_frame)
        self.sales_interface = Sales_interface(self.data, self.content_frame, self.bottom_frame)

    def run(self):
        # logo
        logo = Image.open("./img/bmw-logo.png")
        logo = logo.resize((100, 100))
        logo = ImageTk.PhotoImage(logo)
        lbl_logo = tk.Label(image=logo, width=100, height=100)
        lbl_logo.place(x=60, y=10)

        # titulo
        lbl_title = tk.Label(self.main_frame, text='BMW Delearship', bg='#EEEEEE', font=('Arial', 18, 'bold'))
        lbl_title.place(x=210, y=50)

        save_logo = Image.open("./img/save.png")
        save_logo = save_logo.resize((50, 50))
        save_logo = ImageTk.PhotoImage(save_logo)
        btn_save = tk.Button(self.main_frame, image=save_logo, text="Save", width=80, height=80, bg='#FFFFFF',
                             command=self.data.save_data)
        btn_save.place(x=680, y=25)

        exit_logo = Image.open("./img/salir_logo.png")
        exit_logo = exit_logo.resize((50, 50))
        exit_logo = ImageTk.PhotoImage(exit_logo)
        btn_exit = tk.Button(self.main_frame, image=exit_logo, text="Exit", width=80, height=80, bg='#FFFFFF',
                             command=self.exit_system)
        btn_exit.place(x=880, y=25)

        self.create_treeview()

        self.window.mainloop()

    def exit_system(self):
        self.window.destroy()

    # tree menu
    def create_treeview(self):
        self.tree_frame = tk.Frame(self.main_frame, bg='#4595BE')
        self.tree_frame.place(x=10, y=20 + self.height/6, width=self.width/5, height=self.height - 30 - self.height/6)

        # style treeview
        style = ttk.Style()
        style.theme_use("default")  # Asegúrate de usar un tema que permita personalización

        # Configurar el estilo del Treeview
        style.configure("Custom.Treeview",
                        background="#4595BE",  # Color de fondo
                        foreground="black",  # Color del texto
                        rowheight=25,
                        fieldbackground="#4595BE")  # Fondo de las celdas

        # treeview widget
        self.tree = ttk.Treeview(self.tree_frame, style="Custom.Treeview")
        self.tree.pack(fill="both", expand=True)

        # Cars
        self.tree.insert("", "end", iid="cars", text="Cars")
        self.tree.insert("cars", "end", text="New Car")
        self.tree.insert("cars", "end", text="Delete Car")
        self.tree.insert("cars", "end", text="Edit Car")
        self.tree.insert("cars", "end", text="Search Car")
        self.tree.insert("cars", "end", text="Print All Cars")

        # Employees
        self.tree.insert("", "end", iid="employees", text="Employees")
        self.tree.insert("employees", "end", text="New Employee")
        self.tree.insert("employees", "end", text="Delete Employee")
        self.tree.insert("employees", "end", text="Edit Employee")
        self.tree.insert("employees", "end", text="Search Employee")
        self.tree.insert("employees", "end", text="Print All Employees")

        # Clients
        self.tree.insert("", "end", iid="clients", text="Clients")
        self.tree.insert("clients", "end", text="New Client")
        self.tree.insert("clients", "end", text="Delete Client")
        self.tree.insert("clients", "end", text="Edit Client")
        self.tree.insert("clients", "end", text="Search Client")
        self.tree.insert("clients", "end", text="Print All Clients")

        # Sales
        self.tree.insert("", "end", iid="sales", text="Sales")
        self.tree.insert("sales", "end", text="New Sale")
        self.tree.insert("sales", "end", text="Delete Sale")
        self.tree.insert("sales", "end", text="Edit Sale")
        self.tree.insert("sales", "end", text="Search Sale")
        self.tree.insert("sales", "end", text="Print All Sales")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def on_tree_select(self, event):
        selected_item = self.tree.focus()
        item_text = self.tree.item(selected_item, "text")

        # Mostrar mensaje personalizado
        if item_text == "New Car":
            self.car_interface.new_car()
        elif item_text == "Delete Car":
            self.car_interface.delete_car()
            # messagebox.showinfo("Modelo", "BMW 3 Series: Deportivo y elegante.")
        elif item_text == "Edit Car":
            pass
        elif item_text == "Search Car":
            pass
        elif item_text == "Print All Cars":
            pass
        else:
            pass

        # employees
        if item_text == "New Employee":
            self.sales_man_interface.new_employee()
        elif item_text == "Delete Employee":
            pass
        elif item_text == "Edit Employee":
            pass
        elif item_text == "Search Employee":
            pass
        elif item_text == "Print All Employees":
            pass
        else:
            pass

        # clients
        if item_text == "New Client":
            self.client_interface.new_client()
        elif item_text == "Delete Client":
            pass
        elif item_text == "Edit Client":
            pass
        elif item_text == "Search Client":
            pass
        elif item_text == "Print All Clients":
            pass
        else:
            pass

        # sales
        if item_text == "New Sale":
            self.sales_interface.new_sale()
        elif item_text == "Delete Sale":
            pass
        elif item_text == "Edit Sale":
            pass
        elif item_text == "Search Sale":
            pass
        elif item_text == "Print All Sales":
            pass
        else:
            pass

# brand, model, transmission, color, price, year, km, car_type, fuel, id, stock)
    def show_error(self):
        messagebox.showerror("Error", "Ha ocurrido un problema inesperado!!!")

"""
    T A R E A:
        0. Como chingaso traer los detalles del carro, (Analizar como esta construido el software), como le hago 
        para poder seleccionar el id de ese combo y traerme todos los detalles 
"""

system = Interface()
system.run()
