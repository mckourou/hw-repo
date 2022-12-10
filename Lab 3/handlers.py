from models import Account, BankAccount
from services import UserServices


class UserHandlers:
    services: UserServices

    def __init__(self, services: UserServices):
        self.services = services

    def sign_up(self, name: str, surname: str, account: Account) -> None:
        name = name.strip()
        surname = surname.strip()

        self.services.create_account(name=name, surname=surname, account=account)

    def sign_in(self, name: str, surname: str) -> BankAccount | None:
        name = name.strip()
        surname = surname.strip()

        return self.services.get_account(name=name, surname=surname)

    def addToBankAccount(self, name: str, surname: str, amount: int) -> None:
        self.services.addToBankAccount(name=name, surname=surname, amount=amount)
        print(self.services.toString(name=name, surname=surname))

    def subFromBankAccount(self, name: str, surname: str, amount: int):
        self.services.subFromBankAccount(name=name, surname=surname, amount=amount)
        print(self.services.toString(name=name, surname=surname))

    def moneyConversion(self, name: str, surname: str, currency_from: str, currency_to: str):
        self.services.moneyConversion(name=name, surname=surname, currency_from=currency_from,
                                      currency_to=currency_to)
        print(self.services.toString(name=name, surname=surname))

    def deleteAcc(self, name: str, surname: str):
        return self.services.deleteAcc(name=name, surname=surname)