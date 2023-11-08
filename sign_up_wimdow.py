from tkinter import *


class SignUpWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Окно регистрации')
        self.geometry("300x300-800+300")
        self.name = StringVar()
        self.login = StringVar()
        self.password1 = StringVar()
        self.password2 = StringVar()

        Label(self, text='Name', font=("Calibri", 12)).grid(row=1, sticky=W)
        Label(self, text='Login', font=("Calibri", 12)).grid(row=2, sticky=W)
        Label(self, text='Password', font=("Calibri", 12)).grid(row=3, sticky=W)
        Label(self, text='Password', font=("Calibri", 12)).grid(row=4, sticky=W)


        Entry(self, textvariable=self.name).grid(row=1, column=1)
        Entry(self, textvariable=self.name).grid(row=2, column=1)
        Entry(self, textvariable=self.name).grid(row=1, column=1)

