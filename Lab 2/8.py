def top_up(account:float, sum: float):
    return account + sum

def deduct(account:float, sum:float):
    return account - sum

def convert(account:float, cur_from:str, cur_to:str):
    if cur_from.upper() == "USD":
        account *= 470
    elif cur_from.upper() == "KZT":
        account /= 470
    return account

def print_balance(account:float):
    print(f"Balance: {account}")



account = 500
account = top_up(account, 270)
print_balance(account)

account = deduct(account, 300)
print_balance(account)

account = convert(account, "USD", "KZT")
print_balance(account)

