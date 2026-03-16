# products = [
#     {'name': 'Lenovo X1 Carbon', 'price': 110_000, 'stock': 12},
#     {'name': 'Lenovo Thinkpad', 'price': 89_000, 'stock': 7},
#     {'name': 'Macbook Pro', 'price': 250_000, 'stock': 3},
#     {'name': 'Macbook Air', 'price': 125_000, 'stock': 5},
#     {'name': 'Asus Zenbook', 'price': 150_000, 'stock': 4},
#     {'name': 'Monster Huma', 'price': 55_000, 'stock': 18},
#     {'name': 'Monster Alba', 'price': None, 'stock': 0},
#     {'name': None, 'price': 100_000_000, 'stock': 0},
# ]
#
# def get_data(data: list, product_name: str, stock: bool,start_price: int,end_price:int) -> list | str:
#     temp_list=[]
#
#     for item in data:
#         if item.get('stock') >0:
#             if item.get('name') == product_name and start_price <= item.get('price') <= end_price:
#                 temp_list.add(item)
#             else:
#                 return 'no stock found'
#     if len(temp_list) >0:
#         return temp_list
#     else:
#         return'no product found'
# result = get_data(
#     data=products,
#     product_name='Lenovo X1 Carbon',
#     stock=True,
#     start_price=110_00,
#     end_price=255_00,
# )
# print(result)

#*args
def total(*args):
    return sum(args)

print(total(1, 2, 3))

print(total(9, 8, 12, 45, 23))

print(total())

def concat_str(*args, seperator: str=" "):
    return seperator.join(args)

print(concat_str("burak", 'yılmaz', '36'))
print(concat_str("bugün", 'sınıf', 'mevcudu', 'çok', 'az'))

from datetime import datetime

def sys_log(*args):
    for msg in args:
        print(f'System log: {msg}\nLog Date: {datetime.now()}')

sys_log('Status Code --> 200', 'DB Connection has been lost', 'Passive')

#**kwargs

def get_info(**kwargs):
    return (
        f'Full name: {kwargs.get("full_name")}\n'
        f'ocp: {kwargs.get("ocp")}\n'
        f'title: {kwargs.get("title")}'
    )
print(get_info(full_name='BY'))
print(get_info(full_name='BYA',ocp='IT'))
print(get_info(full_name='BY',ocp='IT',title='MR'))