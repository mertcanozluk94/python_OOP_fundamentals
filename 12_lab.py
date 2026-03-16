from random import randint
def number_generator(amount:int,start_point:int,end_point:int) -> list:
    return[randint (a=start_point,b=end_point) for _ in range(amount)]
def find_even_odd(number_lst: list[int]):
    even_lst= []
    odd_lst= []

    for i in number_lst:
        if i % 2==0:
            even_lst.append(i)
        else:
                odd_lst.append(i)
    return even_lst,odd_lst
nmb=number_generator(amount=100,start_point=0,end_point=9)

even_lst,odd_lst= find_even_odd(number_lst=nmb)
print(even_lst)
print(odd_lst)

#signup valid? sign in,e mail pass,all of this work in main()

users= {
    'xyz@xyz.com' : 'pwd',
    'kerem@krm.com' : 'wddwd',
}

def is_pwd_valid(password: str) -> bool:
    ch_set = set(password)
    print(ch_set)

def is_mail_valid(mail_address: str) -> bool:
    try:
        if '@' not in mail_address:
            raise TypeError("must contain '@'")
        if mail_address in users.keys():
            raise ValueError("this mail already exists")
        return True
    except (TypeError, ValueError) as err:
        print(err)
        return False
def sign_in(mail_address: str, password: str) -> str:
    for key,values in users.items():
        if key == mail_address and values == password:
            return f'{key} is logged in'
        else:
            return 'invalid credentials'
def sign_up(mail_address: str, password: str) -> str:
    if is_pwd_valid(password=password) and is_mail_valid(mail_address=mail_address):
        return 'your membership is ok'
    else:
        return 'wrong credentials'
def main():
    process = input('type your process name:')

    match process:
        case 'sign in':
            print(
                sign_in(
                        mail_address=input('mail address:')
                        , password=input('password:')
            )
                )
        case 'sign up':
            print(
                sign_up(mail_address=input('mail address:')
                        , password=input('password:')
                        )
            )
        case _:
            print('type valid process name')
main()