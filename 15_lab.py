#decorator


# from math import pow,factorial
# from time import time_ns
# def calculate_time_execution(func):
#     def wrapper(*args, **kwargs):
#         start_time = time_ns()
#         func(*args, **kwargs)
#         end_time = time_ns()
#         print(f'performance: {end_time - start_time} ns')
#
#     return wrapper
#
#
# @calculate_time_execution
# def calculate_pow(x:int,y:int):
#         print(f'Result: {pow(x,y)}')
# @calculate_time_execution
# def calc_fact(num:int):
#         print(f'factorial: {factorial(num)}')
# @calculate_time_execution
# def sum_num(x:int,y:int,z:int):
#         return x+y+z
#
#
# calculate_pow(x=4, y=2)
# calc_fact(num=4)
# sum_num(x=4,y=2,z=6)

# from datetime import datetime
#
# def log_info(func):
#     def wrapper(*args, **kwargs):
#         print(
#             f'process name: {func.__name__}\n'
#             f'process time: {datetime.now()}'
#         )
#         return func(*args, **kwargs)
#     return wrapper
#
#
#
# @log_info
# def money_withdraw(account_id: str, amount: int, withdraw: int):
#         amount -= withdraw
#         return(
#             f'this {account_id} , money withdrawed {withdraw} \n'
#             f'current {amount} :D '
#         )
#
# print(
#     money_withdraw(
#         account_id='123',
#         amount=100,
#         withdraw=15,
#     )
# )
#
# @log_info
# def money_deposit(account_id: str, amount: int, deposit: int):
#     amount += deposit
#     return (
#         f'this {account_id} , money deposited {deposit} \n'
#         f'current {amount} :D '
#     )
#
# print(
#     money_deposit(
#         account_id='123',
#         amount=100,
#         deposit=15,
#     )
# )

def is_manager(func):
    def wrapper(user):
        if user.get('role') in ['manager', 'general manager']:
            return func(user)
        else:
            return 'no auth!'
    return wrapper

@is_manager
def get_report(user):
    print(f'{user.get("username")} - {user.get("role")}\n report here..!')

user_1 = {
    'username': 'Hasan Cobanoglu',
    'role': 'manager'
}

user_2 = {
    'username': 'Rana Nur Ceylan',
    'role': 'general manager'
}

user_3 = {
    'username': 'Burak Yilmaz',
    'role': 'Irgat'
}

get_report(user_1)
get_report(user_2)
get_report(user_3)