#abstraction
import dataclasses
from abc import ABC,abstractmethod
from datetime import datetime
#
# class BaseService:
#     def __init__(self, model: str, brand: str):
#         self.model = model
#         self.brand = brand
#
# class Gitar(BaseService):
#     def __init__(self, model: str, brand: str, tel: str):
#         super().__init__(model, brand)
#         self.tel = tel
#
#
# class Keman(BaseService):
#     def __init__(self, model: str, brand: str, case: str):
#         super().__init__(model, brand)
#         self.case = case
#
#
# class Musician:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.played_ins = list()
#
#
# class BaseMusic(ABC):
#
#     @abstractmethod
#     def call_sound(self) -> str:
#         pass
#
#
# class KemanService(BaseMusic):
#         def call_sound(self) -> str:
#             return 'Keman'
#
# k1= KemanService()
# print(k1.call_sound())

class BaseBill:
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.amount = amount
        self.value_add_task = value_add_task
        self.bill_name = bill_name

# @dataclass
#class BaseBill:
    # bill_name:str
    # value_add_task:float
    # amount:float


class WaterBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: int):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill
# @dataclass
# class WaterBill(BaseBill):
#     mill : int


# class NaturalGasBill(BaseBill):
#     def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
#         super().__init__(bill_name, value_add_task, amount)
#         self.m3 = m3
@dataclasses.dataclass
class NaturalGasService(BaseBill):
    m3: float


class ElectricityBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw
# @dataclasses.dataclass
# class ElectricityService(BaseBill):
#     kw: float

class BaseService(ABC):
    @abstractmethod
    def calculate_bill(self,bill: BaseBill) -> float: # we can use our class as type
        pass
    def create_log(self,bill: BaseBill,calculate_bill_result: float) -> str:
        with open(file='bill_2.txt',mode='a',encoding='utf-8') as file:
            file.write(
                f'Bill Name: {bill.bill_name}\n'
                f'Total Amount: {calculate_bill_result}\n'
                f'Payment Date: {datetime.now()}\n'
                f'====================\n'
            )
        return f'{bill.bill_name} payment'
class WaterBillService(BaseService):
    def calculate_bill(self,bill: WaterBill) -> float:
        return bill.value_add_task * bill.amount * bill.mill

class NaturalGasService(BaseService):
    def calculate_bill(self, bill: WaterBill) -> float:
        return bill.value_add_task * bill.amount * bill.m3
class ElectricityService(BaseService):
    def calculate_bill(self, bill: WaterBill) -> float:
        return bill.value_add_task * bill.amount * bill.kw

water_bill = WaterBill(bill_name="serv",value_add_task=10,mill=5,amount=44)
water_bill_service = WaterBillService()
bill_result= water_bill_service.calculate_bill(bill=water_bill)
msg=water_bill_service.create_log(bill=water_bill,calculate_bill_result=bill_result)
print(msg)