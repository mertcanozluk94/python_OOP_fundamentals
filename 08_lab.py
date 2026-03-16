print (
    list(
        map(lambda x: x **2, [i for i in range(10)])
    )
)

print(
    list(
        map(str,[i for i in range(10)])
    )

)

listex= [
    ['kerem',15,59.49],
    ['aysen',25,35.43],
    ['ihvan',44,33.33],
]

print(
    list(
        map(lambda x: x[2]* 1.10,listex)
    )
)

from random import randint
numbers = [randint(-100,100) for i in range(10)]
positive_str= list(
    map(
        str,
    filter(lambda x: x > 0 ,numbers)
    )
)
print(positive_str)

str_result='-'.join(positive_str)
print(positive_str)
