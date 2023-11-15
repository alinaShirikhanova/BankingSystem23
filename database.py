import sqlite3

from bank_account import BankAccount


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('BankSystem.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        login NOT NULL UNIQUE,
        password NOT NULL,
        balance INTEGER
        );''')

    def insert_account(self, name, login, password):
        self.cursor.execute('INSERT INTO accounts(name, login, password, balance) values(?, ?, ?, ?)',
                            (name, login, password, 0))
        self.connection.commit()



