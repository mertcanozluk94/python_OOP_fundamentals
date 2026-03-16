#Encapsulation
from uuid import uuid4
from datetime import datetime
from socket import gethostname,gethostbyname
from enum import Enum
from pprint import pprint

from streamlit.web.server.server import start_listening_tcp_socket


class Status(Enum):
    Active=1
    Modified=2
    Passive=3

class BaseEntity:
    def __init__(self):
        self.__id= None
        self.__name= None
        self.__value= None
    hello= 1

    def set_values_private_attributes(self):
        self.__id= uuid4()
        self.__create_date=datetime.now()
        self.__computer_name= gethostname()
        self.__ip_address= gethostbyname(gethostname())
        self.__status= Status.Active

class Supplier(BaseEntity):
    pass

class Product(BaseEntity):
    def __init__(self,name:str,desc:str):
        super().__init__()
        self.desc= desc
        self.name= name
        self.__price= None
        self.__stock= None
    def set_values_private_attributes(self,price:float,stock:float):
        if price > 0 and stock >0:
            super().set_values_private_attributes()
            self.__price=price
            self.__stock=stock
            print('product has been created')
            pprint(self.__dict__)
        else:
            print('invalid input')
p1 = Product(name="kerem",desc="aaa")
p1.set_values_private_attributes(price=50,stock=25)