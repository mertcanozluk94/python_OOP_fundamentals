from importlib.resources.readers import remove_duplicates


def sumx(a,b):
    print(a+b)

sumx(3,5)

def toplam(a: int, b: int):
    """ 
    this func adds two numbers
    Args:
    a (int): first number
    b (int): second number
    """
    print(a+b)
    print(a*b)
    print(a/b)
    print(a-b)
toplam(5,9)

# def sirket(full_name: str, domain: str = '@outlook.com'):
#     names= full_name.lower().split(' ')
#     print(f'mail adres: {names[0]}.{names[-1]}{domain}')
#
# sirket(
#     full_name= 'tello can',
#     domain = '@xyz.com',
# )
#
# def multiply(a: int, b: int ,c: int):
#     print(a*b*c)
#
# multiply(3,5,5)

# def sum_numbers(x: int,y: int,z:int) -> int:
#     return x+y+z
# sum_result = sum_numbers(
#     x=int(input("first num:")),
#     y=int(input("second num:")),
#     z=int(input("third num:")),
# )
# print(sum_result)

def remove_duplicate_word(sentence: str) -> str:
#path 1
    lst=[]
    for item in sentence.split():
        if item not in lst:
            lst.append(item)

    str_output= " ".join(lst)
    return str_output
result= remove_duplicate_word(sentence="merhaba ben burak merhaba ben burak")
print(result)
#path 2
lst_1= [item for item in sentence.split()]
lst_2= set(lst_1)
str_output=' '.join(lst_2)
print(str_output)
#path_3
return ' '.join(set([item for item in sentence.split()])
result= remove_duplicate_word(sentence='merhaba ben burak merhaba ben burak')
print(result)
