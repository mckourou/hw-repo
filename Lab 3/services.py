from models import Account, BankAccount
from repositories import UserRepositories


class UserServices:
    repositories: UserRepositories

    def __init__(self, repositories: UserRepositories):
        self.repositories = repositories

    def create_account(self, name: str, surname: str, account: Account) -> None:
        self.repositories.create_account(name=name, surname=surname, account=account)

    def get_account(self, name: str, surname: str) -> BankAccount | None:
        return self.repositories.get_account(name=name, surname=surname)

    def addToBankAccount(self, name: str, surname: str, amount: int) -> None:
        self.repositories.addToBankAccount(name=name, surname=surname, amount=amount)

    def subFromBankAccount(self, name: str, surname: str, amount: int) -> None:
        self.repositories.subFromBankAccount(name=name, surname=surname, amount=amount)

    def moneyConversion(self, name: str, surname: str, currency_from: str, currency_to: str):
        self.repositories.moneyConversion(name=name, surname=surname,currency_from=currency_from,
                                          currency_to=currency_to)

    def toString(self, name: str, surname: str):
        return self.repositories.toString(name=name, surname=surname)

    def deleteAcc(self, name: str, surname: str):
        return self.repositories.deleteAcc(name=name, surname=surname)
