
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

    def new_employee(self):
        self.new_frame = tk.Frame(self.content_frame, width=self.content_frame.winfo_width(),
                                  height = self.content_frame.winfo_height(), bg='#484b4c')

        self.new_label_frame = tk.LabelFrame(self.new_frame, text="New Employee",
                                             bg='#484b4c',
                                             width=self.content_frame.winfo_width() - 10,
                                             height = self.content_frame.winfo_height() - 10,
                                             fg='white')
        self.new_label_frame.place(x=5, y=5)
        # Model
        lbl_model = tk.Label(self.new_label_frame, bg='#484b4c', text='Name: ')
        lbl_model.place(x=20, y=20)
        self.txt_model = tk.Entry(self.new_label_frame, width=20)
        self.txt_model.place(x=120, y=20)

        # Brand
        lbl_brand = tk.Label(self.new_label_frame, bg='#484b4c', text='Last name: ')
        lbl_brand.place(x=20, y=50)
        self.txt_brand = tk.Entry(self.new_label_frame, width=20)
        self.txt_brand.place(x=120, y=50)