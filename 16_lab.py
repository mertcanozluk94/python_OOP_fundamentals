hakan_account = {
    'account no': '98765',
    'password': '546',
    'balance': 3000,
    'additional balance': 1000
}

ipek_account = {
    'account no': '34567',
    'password': '987',
    'balance': 4000,
    'additional balance': 1000
}

burak_account = {
    'account no': '345627',
    'password': '9487',
    'balance': 3000,
    'additional balance': 1000
}

users = [burak_account, hakan_account, ipek_account]

# money withdraw
# 1. balance>amount you can withdraw
# 2. if not
# 2.1. additional balance
# 2.1.1 if say yes you can withdraw add. bal.
# 2.1.1.1. all money
# 2.1.2. if says no its gonna cancel

def get_valid_answer(question:str, valid_options: tuple) -> str:
    question += f'({"," .join(valid_options)}):'
    response = input(question)
    while response.lower() not in valid_options:
        print('Please enter a valid option')
        response = input(question)

    return response
def account_information(account:dict):
    print(
        f'Account no: {account["account no"]}\n'
        f'Balance: {account["balance"]}\n'
        f'Additional Balance: {account["additional balance"]}\n'
    )


def withdraw_money(account: dict, amount: int):
    if account['balance'] >= amount:
        account['balance'] -= amount
        account_information(account=account)
        print('dont forget your money')
    else:
        total_balance = account['balance'] + account['additional balance']

        if total_balance >= amount:
            used_additional_balance = input('Insufficen balance..!\nDo you want to use additional balance? ("y", "n")')

            match used_additional_balance:
                case 'y':
                    detech_amount= amount - account['balance']
                    account['balance']=0
                    account['additional balance'] -= detech_amount
                    account_information(account=account)
                    print('dont forget your money')
                case 'n':
                    print('Transaction has been cancelled..!')
                    account_information(account=account)
        else:
            print(
                'Insufficient balance..!\n'
                'Transaction has been cancelled..!'
            )
            account_information(account=account)

withdraw_money(account=hakan_account, amount=4000)

def deposit_money(account: dict, amount: int):
    account['balance'] += amount
    account_information(account=account)
    if account['additional balance'] < 1000:
        short_additional = 1000 - account['additional balance']
        account['balance'] -= short_additional
        account['additional balance'] += short_additional
    else:
        account['balance'] -= amount
        account['additional balance'] += amount
    account_information(account=account)

deposit_money(burak_account, amount=1000)