numbers = [3233,4244,115,1616,7347347,324234,22]
result = any(numbers <120 for numbers in numbers)
print(result)


pls = ['java','linux','python','ubuntu']
print(
    any(pl == 'windows' for pl in pls)
)

names = ['ali','veli','beli']
age = [22,11,55]
city = ["ankara","bursa","cankiri"]

result= list (
    zip(names,age,city)
)
print(result)

from random import randint
number_1 = [randint(1,100 ) for i in range(10)]
number_2 = [randint(1,100) for i in range(10)]

temp_list=(
    zip(number_1,number_2)
)