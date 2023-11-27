from tkinter import *

from database import Database


class LogInWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Окно авторизации')
        self.geometry("300x300-800+300")
        self.login = StringVar()
        self.password = StringVar()
        self.database = Database()

        self.notif = Label(self, font=("Calibri", 12))
        self.notif.grid(row=5, sticky=W)


        Label(self, text='Login', font=("Calibri", 12)).grid(row=2, sticky=W)
        Label(self, text='Password', font=("Calibri", 12)).grid(row=3, sticky=W)

        Entry(self, textvariable=self.login).grid(row=2, column=1)
        Entry(self, textvariable=self.password).grid(row=3, column=1)


        Button(self, text="Log In", font=("Calibri", 12), width=15, command=self.log_in).grid(row=6, sticky=W)

    def log_in(self):
        self.notif.config(text='')
        login = self.login.get()
        user_details = self.database.get_user_by_login(login)
        if user_details is not None:
            if user_details[3] == self.password.get():
                self.notif.config(text='Вы успешно авторизованы', fg='green')

