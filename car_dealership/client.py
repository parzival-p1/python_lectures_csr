
class Client:
    def __init__(self, id, name, last_name, vip):
        self.name = name
        self.last_name = last_name
        self.vip = vip
        self.id = id

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_vip(self):
        return self.vip

    def set_vip(self, vip):
        self.vip = vip

    def get_id(self):
        return self.id

    def __str__(self):
        data = "\nID: " + str(self.id) + "\nName: " + self.name + "\nLast name: " + self.last_name + "\Vip: " + self.vip
        return data