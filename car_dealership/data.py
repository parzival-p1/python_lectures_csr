import os
from operator import index
from re import search

import pandas as pd

class Data:
    def __init__(self): # brand, model, transmission, color, price, year, km, car_type, fuel, id, stock
        self.car_columns = ['ID', 'Brand', 'Model', 'Transmission', 'Color', 'Price', 'Year', 'Km', 'Car Type',
                            'Fuel', 'Stock']
        self.df_cars = pd.DataFrame(columns = self.car_columns)
        self.client_columns = ['ID', 'Name', 'Last Name', 'Phone Number', 'Address', 'Email', 'Gender', 'Birthday']
        self.df_clients = pd.DataFrame(columns = self.client_columns)
        self.salesman_columns = ['ID', 'Name', 'Last Name', 'Phone Number', 'Address', 'Email', 'Gender', 'Birthday']
        self.df_salesmen = pd.DataFrame(columns = self.salesman_columns)
        self.car_id = 1000
        self.client_id = 2000
        self.sales_id = 3000
        self.sales_man_id = 4000

    def add_car(self, new_car):
        new_index = len(self.df_cars)
        self.df_cars.loc[new_index] = list(new_car.values())
        print("Estoy en add car",self.df_cars)
        self.car_id += 1

    def add_client(self, new_client):
        new_index = len(self.df_clients)
        self.df_clients.loc[new_index] = list(new_client.values())
        # print("Estoy en add_client", self.df_clients)
        self.client_id += 1

    def add_salesman(self, new_salesman):
        new_index = len(self.df_salesmen)
        self.df_salesmen.loc[new_index] = list(new_salesman.values())
        # print("Estoy en salesman", self.df_salesmen)
        self.sales_man_id += 1

    def get_car_data_by_id(self, id):
        return  self.df_cars.loc[self.df_cars['ID'] == id]

    def get_client_data_by_id(self, id):
        return  self.df_clients.loc[self.df_clients['ID'] == id]

    def get_salesman_data_by_id(self, id):
        return  self.df_salesmen.loc[self.df_salesmen['ID'] == id]

    def delete_car_by_id(self, id):
        self.df_cars = self.df_cars[self.df_cars['ID'] != id]
        print(self.df_cars)

    def delete_client_by_id(self, id):
        self.df_clients = self.df_clients[self.df_clients['ID'] != id]

    def delete_salesman_by_id(self, id):
        self.df_salesmen = self.df_salesmen[self.df_salesmen['ID'] != id]

    def edit_car(self, df_update):
        self.df_cars.loc[self.df_cars["ID"] == df_update['ID'], list(df_update.keys())] = list(df_update.values()) # REVISAR EL JUEVES

    def edit_client(self, df_update):
        self.df_clients.loc[self.df_clients["ID"] == df_update['ID'], list(df_update.keys())] = list(df_update.values())

    def edit_salesman(self, df_update):
        self.df_salesmen.loc[self.df_salesmen["ID"] == df_update['ID'], list(df_update.keys())] = list(df_update.values())

    def get_next_car_id(self):
        return self.car_id

    def get_next_client_id(self):
        return self.client_id

    def get_next_salesman_id(self):
        return self.sales_man_id

    def save_data(self):
        # Guardar en un archivo Excel con varias hojas
        with pd.ExcelWriter("car_dealership.xlsx", engine="openpyxl") as writer:
            self.df_cars.to_excel(writer, sheet_name="Cars", index=False)
            self.df_clients.to_excel(writer, sheet_name="Clients", index=False)
            self.df_salesmen.to_excel(writer, sheet_name="Salesmen", index=False)

    def load_data(self):
        if os.path.exists("car_dealership.xlsx"):
            df_dict = pd.read_excel("car_dealership.xlsx", sheet_name=None, dtype=str)
            # df_dict es un diccionario con cada hoja como un DataFrame
            self.df_cars = df_dict["Cars"]
            self.car_id = int(self.df_cars["ID"].max()) + 1
            self.df_clients = df_dict["Clients"]
            self.client_id = int(self.df_clients["ID"].max()) + 1
            self.df_salesmen = df_dict["Salesmen"]
            self.sales_man_id = int(self.df_salesmen["ID"].max()) + 1

    def print_data(self):
        print(self.df_cars)
        print(self.df_salesmen)
        print(self.df_clients)
