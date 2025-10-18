
class Car:
    # variable estatica que pertenece a la clase pero no al objeto (todos los objetos pueden verla y modificar)
    def __init__(self, brand, model, transmission, color, price, year, km, car_type, fuel, id, stock):
        self.brand = brand
        self.model = model
        self.transmission = transmission
        self.color = color
        self.price = price
        self.year = year
        self.km = km
        self.car_type = car_type
        self.fuel = fuel
        self.id = id
        self.stock = stock

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_transmission(self):
        return self.transmission

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_year(self):
        return self.year

    def get_km(self):
        return self.km

    def car_type(self):
        return self.car_type

    def get_fuel(self):
        return self.fuel

    def get_id(self):
        return self.id

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock

    def __str__(self):
        data = "\nID: " + str(self.id) + "\nBrand: " + self.brand + "\nModel: " + self.model + "\nTransmission: \n" + self.transmission
        data += "\nColor: " + self.color + "\nYear: " + str(self.year) + "\nKilometres: " + str(self.km)
        data +=  "\nCar type: " + self.car_type + "\nFuel: " + self.fuel + "\nPrice: $" + str(self.price) + "\nStock: " + str(self.stock)
        return data