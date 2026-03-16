import datetime


class BaseBill:
    def __init__(self, bill_name: str,value_add_task: float,amount:float):
        self.bill_name = bill_name
        self.value_add_task = value_add_task
        self.amount = amount
    def calculate_bill(self):
        return self.value_add_task * self.amount
    def create_log(self):
        with open(file='bill_info.txt',mode='a',encoding='utf-8') as file:
            file.write(
                f'Bill Name: {self.bill_name}\n'
                f'Total Amount: {self.calculate_bill()}\n'
                f'Payment Date: {datetime.time()}\n'
                f'====================\n'
            )
class Waterbill(BaseBill):
    def __init__(self,bill_name:str,value_add_task:float,amount:float,mill:int):
        super().__init__(bill_name,value_add_task,amount)
        self.mill = mill
    def show_info(self):
        print(
            f'bill_name: {self.bill_name}, value_add_task: {self.value_add_task}, amount: {self.amount}'
        )
    def calculate_bill(self):
        return super().calculate_bill() * self.mill

class NaturalGasBill(BaseBill):
    def __init__(self,bill_name:str,value_add_task:float,amount:float,m3: float):
        super().__init__(bill_name,value_add_task,amount)
        self.m3 = m3

    def calculate_bill(self):
        return super().calculate_bill() * self.m3

class ElectricBill(BaseBill):
    def __init__(self,bill_name:str,value_add_task:float,amount:float,kw: float):
        super().__init__(bill_name,value_add_task,amount)
        self.kw = kw

water_bill = Waterbill(bill_name='ssAS',value_add_task=4.5,amount=3.5,mill=4)
water_bill.create_log()

naturel_gas_bill= NaturalGasBill(bill_name='IGDAS',value_add_task=3.5,amount=3.5,m3=4)
naturel_gas_bill.create_log()