import tkinter as tk
from data import Data
from PIL import Image, ImageTk

class Interface:
    def __init__(self):
        # window
        self.width = 1000
        self.height = 700
        self.window = tk.Tk() # crea obj de tipo Tk (es la ventana)
        self.window.config(width=self.width, height=self.height, bg="#FF0000")
        self.window.title("Car Dealership System")
        self.window.resizable(width=False, height=False)

        # main frame
        self.main_frame = tk.Frame(self.window, width=self.width, height=self.height, bg='#000000')
        self.main_frame.pack(fill="both", expand=True)

        # top bar
        self.top_bar_frame = tk.Frame(self.main_frame, width=self.width-20, height=self.height/6, bg='#ff0000')
        self.top_bar_frame.place(x=10, y=10)

        # left bar
        self.left_bar_frame = tk.Frame(self.main_frame, width=self.width/5, height=self.height - 30 - self.height/6, bg='#00ff00')
        self.left_bar_frame.place(x=10, y=20 + self.height/6)

        # content frame
        self.content_frame = tk.Frame(self.main_frame, width=self.width - 30 - self.width/5, height=4 * self.height/6, bg='#0000ff')
        self.content_frame.place(x=20 + self.width/5, y=20 + self.height/6)

        # bottom frame
        self.bottom_frame = tk.Frame(self.main_frame, width=self.width - 30  - self.width/5, height=self.height/10, bg='#ffff00')
        self.bottom_frame.place(x=20 + self.width/5, y=30 + (5 * self.height)/6)


        self.data = Data() # main obj that contains all the info


    def run(self):

        # logo
        logo = Image.open("./img/bmw-logo.png")
        logo = logo.resize((100, 100))
        logo = ImageTk.PhotoImage(logo)
        lbl_logo = tk.Label(image=logo, width=100, height=100)
        lbl_logo.place(x=10, y=10)

        btn_test = tk.Button(self.window, text="test", width=20, height=3)
        btn_test.place(x=200, y=50)

        self.window.mainloop()

system = Interface()
system.run()
