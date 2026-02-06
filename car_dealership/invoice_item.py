import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Invoice_item:
    count = 1

    def __init__(self, main_frame, dict_cars, owner, y):
        self.row_id = Invoice_item.count
        Invoice_item.count += 1
        self.main_frame = main_frame
        self.dict_cars = dict_cars
        self.width = main_frame.winfo_width() - 10
        self.height = main_frame.winfo_height() / 7
        self.owner = owner
        self.y = y

    def show_row(self):
        self.row_frame = tk.Frame(self.main_frame,  width=self.width, height=self.height, bg='#484b4c')
        self.txt_car_id = ttk.Combobox(self.row_frame, width=10, state="readonly",
                                         values=list(self.dict_cars.keys()))
        self.txt_car_id.place(x=5, y=5)

        self.lbl_car_description = tk.Label(self.row_frame, bg='#484b4c', fg="white", text='')
        self.lbl_car_description.place(x=100, y=5)

        self.txt_car_stock = ttk.Combobox(self.row_frame, width=10, state="readonly",
                                         values=["1", "2", "3"])
        self.txt_car_stock.place(x=620, y=5)
        self.btn_delete_concept = tk.Button(self.row_frame, text="Delete", width=5, command=self.delete_row)
        self.btn_delete_concept.place(x=700, y=5)
        self.row_frame.place(x=5, y=self.y)

    def get_selected_data(self):
        if self.txt_car_id == "":
            messagebox.showerror("Error!", "No se ha seleccionado un concepto")
        elif self.txt_car_stock == "":
            messagebox.showerror("Error!", "No se ha seleccionado un cantidad")
        else:
            return self.txt_car_id.get(), self.txt_car_stock.get()
        return 0, 0

    def delete_row(self):
        # self.row_frame.destroy()
        self.owner.remove_item(self)