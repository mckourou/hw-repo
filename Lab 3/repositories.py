import models
from models import BankAccount, Account


class UserRepositories:
    users: list[BankAccount] = []

    def create_account(self, name: str, surname: str, account: Account) -> None:
        user = BankAccount(name=name, surname=surname, account=account)
        self.users.append(user)

    def get_account(self, name: str, surname: str) -> BankAccount | None:
        user = next((u for u in self.users if name == u.name and surname == u.surname), None)

        if not user:
            print('User not found')
            return

        return user

    def addToBankAccount(self, name: str, surname: str, amount: int) -> None:
        BankAccount.addToBankAccount(self.get_account(name=name, surname=surname), amount=amount)

    def subFromBankAccount(self, name: str, surname: str, amount: int) -> None:
        BankAccount.subFromBankAccount(self.get_account(name=name, surname=surname), amount=amount)

    def moneyConversion(self, name: str, surname: str, currency_from: str, currency_to: str) -> None:
        user = self.get_account(name=name, surname=surname)
        if currency_from.upper() == user.account.value:
            BankAccount.moneyConversion(user, currency_from=currency_from, currency_to=currency_to)
        else:
            print("Sorry, something went wrong")

    def toString(self, name: str, surname: str):
        return BankAccount.__repr__(self.get_account(name=name, surname=surname))

    def deleteAcc(self, name: str, surname: str):
        user = self.get_account(name=name, surname=surname)
        self.users.remove(user)
        return BankAccount.__del__(user)
