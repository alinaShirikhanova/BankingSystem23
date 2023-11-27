from tkinter import *
import os




class LoginSession(Toplevel):
    def __init__(self, parent, user_name, user_login, user_password):
        super().__init__(parent)
        self.title('LoginSession')
        self.geometry('300x300-800+300')
        self.parent = parent
        self.name = user_name
        self.login = user_login
        self.password = user_password
        self.balance = self.get_current_balance()

        Label(self, text=f'Здравствуйте, {self.name}', font=('Calibri', 13)).pack(side=TOP, pady=10)

        Label(self, text=f'Ваш баланс: {self.balance}', font=('Calibri', 13)).pack(side=TOP)

        Button(self, text='Внести', font=('Calibri', 12), width=15, command=self.deposit).pack(side=TOP, pady=10)


    def get_current_balance(self):
        with open(self.login, 'r') as f:
            f = f.read().split('\n')
            balance = f[3]
        return balance

    # def deposit(self):
    #     UpdateBalance(self.parent, self.name, self.login, self.password, self.balance)