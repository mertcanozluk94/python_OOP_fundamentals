numbers = [1,4,5,67,8,3]

print(
    set(numbers)
)

full_name= 'nelson'
unique_ch = list(set(full_name))
unique_ch.sort()
print(unique_ch)

boxers = {'momi','flex','chama','sincara'}
boxers.discard('fl')
boxers.remove('flex')
print(boxers)

#pop and remove different . pop = index , remove = "word"

password = 'Bu?R4k'

is_password_valid= [
        any(ch.isupper() for ch in password),
        any(ch.islower() for ch in password),
        any(ch.isdigit() for ch in password),
        any(not ch.isalnum() for ch in password),
]

print (
    all(is_password_valid)
)

dictt = {
    "kerem": 1,
    "ozgur": 2,
    "talisca":3,
    "matruska":4,
}
print(dictt)

for value in dictt.values():
    print(value)
for key in dictt.keys():
    print(key)

print(
    dictt['kerem']
)
print(
    dictt.get('ozgur') #more secure and not given error.
)
dictt.update({'kerem':5})
print(
    dictt.get('kerem')
)
#set

products = [
    {'name': 'Lenovo X1 Carbon', 'price': 110.000},
    {'name': 'Lenovo Thinkpad', 'price': 89.000},
    {'name': 'Macbook Pro', 'price': 250.000},
    {'name': 'Macbook Air', 'price': 125.000},
    {'name': 'Asus Zenbook', 'price': 150.000},
    {'name': 'Monster Huma', 'price': 55.000},
]

total_price = sum(product.get('price') for product in products)
print(f' Total Price: {total_price}')

wanted_price = 200.000
selected_products = [product for product in products if product.get('price',0) > wanted_price]
print(f' Bigger price: {selected_products}')

for product in products:
    print(
        f'product name: {product["name"]}\n'
        f'price: {product["price"]}'
    )

name= 'Lenovo'
min_price= 100.000
max_price= 150.000
sp_2= [product for product in products if name in product.get('name','') and min_price < product.get('price',0) < max_price ]

for product in sp_2:
    print(
        f'new product name: {product["name"]}\n'
        f'new price: {product["price"]}'
    )

