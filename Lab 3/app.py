import sys
from textwrap import dedent

from handlers import UserHandlers
from models import Account
from repositories import UserRepositories
from services import UserServices


def init():
    user_repositories = UserRepositories()
    user_services = UserServices(repositories=user_repositories)
    user_handlers = UserHandlers(services=user_services)

    while True:
        text = '''
        Выберите Ваше действие: 
        1. Создание пользователя
        2. Выбрать пользователя
        q - чтобы выйти
        '''
        print(dedent(text))
        command = input()

        if command == 'q':
            sys.exit(0)

        if command == '1':
            name, surname = input('Enter name and surname: ').split()
            user_handlers.sign_up(name=name, surname=surname, account=Account.KZT)

        elif command == '2':
            name, surname = input('Enter name and surname: ').split()
            user = user_handlers.sign_in(name=name, surname=surname)

            if user:

                while True:
                    text_2 = '''
                    Выберите Ваше действие: 
                        1. Пополнить аккаунт
                        2. Снять с аккаунта
                        3. Конвертация
                        4. Удалить аккаунт
                        q - чтобы выйти
                    '''
                    print(dedent(text_2))
                    command_2 = input()

                    if command_2 == 'q':
                        break

                    if command_2 == '1':
                        amount = int(input("Введите сумму: "))
                        user_handlers.addToBankAccount(name=name, surname=surname, amount=amount)

                    elif command_2 == '2':
                        amount = int(input("Введите сумму: "))
                        user_handlers.subFromBankAccount(name=name, surname=surname, amount=amount)

                    elif command_2 == '3':
                        currency_from = input("С какой валюты желаете конвертировать: ")
                        currency_to = input("На какую валюту желаете конвертировать: ")
                        user_handlers.moneyConversion(name=name, surname=surname, currency_from=currency_from,
                                                      currency_to=currency_to)

                    elif command_2 == '4':
                        user_handlers.deleteAcc(name=name, surname=surname)
                        break

                    else:
                        print("Incorrect, please try again")

        else:
            print("Incorrect, please try again")

if __name__ == '__main__':
    init()