from tkinter import *

from PIL import Image, ImageTk

from sign_up_wimdow import SignUpWindow


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Мобильный банк")
        self.geometry("300x300-800+300")
        image = Image.open('data/bank.PNG').resize((170, 170))
        self.img = ImageTk.PhotoImage(image)

        Label(self, text='Самый безопасный в мире банк!', font=("Calibri", 13)).pack(side=TOP)
        Label(self, image=self.img).pack(side=TOP)

        Button(self, text="Sign Up", font=("Calibri", 12), width=15, command=self.create_sign_up_window).pack(side=TOP, pady=5)

    def create_sign_up_window(self):
        SignUpWindow()
            





