#inherit
from pyarrow import show_info


# class Human:
#     def __init__(self, full_name:str , weight: int | float , height: int | float):
#         self.full_name = full_name
#         self.weight = weight
#         self.height = height
#     def show_info(self):
#         return self.__dict__
# class FootSoldier(Human):
#     pass
# class Knight(Human):
#     pass
# fs_1 = FootSoldier(full_name="burak", weight=100, height=200)
# print(fs_1.show_info())


##########


# class BaseEntity:
#     def __init__(self, full_name:str , desc:str):
#         self.full_name = full_name
#         self.desc = desc
#     def show_info(self):
#         print(
#             f'name {self.full_name}'
#             f'description{self.desc})'
#         )
# class Category(BaseEntity): #we can add multi class.
#     pass
# class Product(BaseEntity):
#     def __init__(self,full_name,desc,price: float,stock : int):
#         super().__init__(full_name,desc) # adding main class utilities - super
#         self.price = price
#         self.stock = stock
# p1 = Product(full_name= "gloves",desc='boxing',price=44,stock=3)
# print(p1.__dict__)
#     def show_info(self):
#         super()show.info()
#         print(
#             f'Price: {self.price}, stock: {self.stock}'
#         )

class BasePhone:
    def __init__(self,phone_id: str,model: str,brand: str,price:float):
        self.phone_id = phone_id
        self.model = model
        self.brand = brand
        self.price = price
    def show_info(self):
        print(
        f'id: {self.phone_id}, model: {self.model}, price: {self.price}'
        )
    def phone_ring_sound(self) -> str:
        return 'phone sound'

class iphone(BasePhone):
    def __init__(self,airdrop: str,phone_id: str,model: str,brand: str,price: float):
        super().__init__(phone_id,model,brand,price)
        self.airdrop = airdrop
    def show_info(self):
        super().show_info()
        print(f'Airdrop: {self.airdrop}')
    def phone_ring_sound(self):
        return 'Iphone phone sound'

class samsung(BasePhone):
    def __init__(self, phone_id: str,model: str,brand: str,price: float,os :str):
        super().__init__(phone_id, model, brand, price)
        self.os = os
    def show_info(self):
        super().show_info()
        print(f'OS: {self.os}')
    def phone_ring_sound(self):
        return 'samsung phone sound'

s_1= samsung(phone_id=3,model='s20',brand='samsung',price=355.00,os='android')
s_1.show_info()
print(s_1.phone_ring_sound())

i_1= iphone(phone_id=4,model='5s',brand='iphone',price=355.00,airdrop='True')
i_1.show_info()
print(i_1.phone_ring_sound())

