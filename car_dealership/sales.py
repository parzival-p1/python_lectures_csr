
class Sales:
    def __init__(self, client_id, car_id, sales_man_id, day, month, year):
        self.client = client_id
        self.car = car_id
        self.sales_man = sales_man_id
        self.day = day
        self.month = month
        self.year = year

    def get_client(self):
        return self.client

    def get_car(self):
        return self.car

    def get_sales_man(self):
        return self.sales_man

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def __str__(self):
        data = "\nClient ID: " + str(self.client) + "\nCar ID: " + str(self.car) + "\nSales man ID: " + str(self.sales_man)
        data += "\nSale date: " + str(self.day) + "/" + str(self.month) + "/" + str(self.year)
        return data