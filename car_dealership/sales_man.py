
class Sales_man:
    def __init__(self, id, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary
        self.id = id

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_salary(self):
        return self.salary

    def get_id(self):
        return self.id

    def __str__(self):
        data = "\nID: " + str(self.id) + "\nName: " + self.name + "\nLast name: " + self.last_name + "\nSalary: " + str(self.salary)
        return data