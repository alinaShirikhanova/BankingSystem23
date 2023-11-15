from tkinter import *

from database import Database


class SignUpWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Окно регистрации')
        self.geometry("300x300-800+300")
        self.name = StringVar()
        self.login = StringVar()
        self.password1 = StringVar()
        self.password2 = StringVar()
        self.database = Database()

        self.notif = Label(self, font=("Calibri", 12))
        self.notif.grid(row=5, sticky=W)

        Label(self, text='Name', font=("Calibri", 12)).grid(row=1, sticky=W)
        Label(self, text='Login', font=("Calibri", 12)).grid(row=2, sticky=W)
        Label(self, text='Password', font=("Calibri", 12)).grid(row=3, sticky=W)
        Label(self, text='Password', font=("Calibri", 12)).grid(row=4, sticky=W)

        Entry(self, textvariable=self.name).grid(row=1, column=1)
        Entry(self, textvariable=self.login).grid(row=2, column=1)
        Entry(self, textvariable=self.password1).grid(row=3, column=1)
        Entry(self, textvariable=self.password2).grid(row=4, column=1)

        Button(self, text="Sign Up", font=("Calibri", 12), width=15, command=self.register_user).grid(row=6, sticky=W)

    def register_user(self):
        self.notif.config(text='')
        # self.name.get() ==  self.name.get().capitalize() - возвращает строку с первой заглавной и остальными маленькими


        c3 = self.check_password()
        c2 = self.check_login()
        c1 = self.check_name()
        if c1 and c2 and c3:
            self.database.insert_account(self.name.get(), self.login.get(), self.password1.get())


    def check_name(self):
        name_is_correct = True
        name = self.name.get()
        correct_len = len(name) > 1
        correct_symbols = self.contains_forbidden_syms(name, '!@#$%^&*()-=_+?/><.,~`1234567890')

        if not correct_symbols:
            name_is_correct = False
            self.notif.config(text='Имя содержит некорректные символы', fg='red')

        if not correct_len:
            name_is_correct = False
            self.notif.config(text='Неккоректная длина имени', fg='red')
        return name_is_correct

    def check_login(self):
        login_is_correct = True
        login = self.login.get()
        correct_symbols_login = self.contains_forbidden_syms(login,
                                                             'абвгдежзийклмнопрстуфхцчшщьыъэюя!#$%^&*()-=_+?/><,~`')
        correct_len_login = len(login) >= 8

        if not correct_len_login:
            login_is_correct = False
            self.notif.config(text='Неккоректная длина логина', fg='red')

        if not correct_symbols_login:
            login_is_correct = False
            self.notif.config(text='Логин содержит некорректные символы', fg='red')
        return login_is_correct

    def check_password(self):
        password1 = self.password1.get()
        password2 = self.password2.get()

        correct_len_password = len(password1) >= 8

        if password1 != password2:
            self.notif.config(text='Пароли не совпадают', fg='red')

        if not correct_len_password:
            self.notif.config(text='Неккоректная длина пароля', fg='red')

    def contains_forbidden_syms(self, line, forb_syms):
        for sym in line:
            if sym in forb_syms:
                return False
        return True

