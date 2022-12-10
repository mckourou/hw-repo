from enum import Enum


class Account(Enum):
    KZT = 'KZT'
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'


class BankAccount:
    name: str
    surname: str
    account: Account
    currency: dict = {
        'EUR': 490,
        'USD': 470,
        'RUB': 7.3,
    }

    def __init__(self, name: str, surname: str, account: Account):
        self.name = name
        self.surname = surname
        self.account = account
        self.balance = 0

    def addToBankAccount(self, amount: int):
        self.balance += amount

    def subFromBankAccount(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount

    def moneyConversion(self, currency_from: str, currency_to: str):  # Только KZT->USD,EUR,RUB или наоборот
        match currency_from:
            case 'KZT':
                self.balance /= self.currency[currency_to]
                self.account = Account[currency_to]
            case _:
                self.balance *= self.currency[currency_from]
                self.account = Account[currency_to]

    def __repr__(self):
        return f"{self.name} {self.surname}'s account has {self.account.value} {self.balance:.2f}"

    def __del__(self):
        print(f"{self.name} {self.surname}'s account has been deleted")

