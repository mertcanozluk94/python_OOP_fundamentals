# class car:
#     door_number = 0
#     engine_size = 5.5
#     torque= 400
#     length = 2500
#     width = 1200
#     brand = 'Dodge'
#     color = 'red'
#     model = 'x5'
#
# c1= car()
# c1.torque = 1000
# print({f'Brand: {c1.brand}  model: {c1.model}'})
# print(car.__dict__)
# print(car.__init__("Dodge"))
#
# class Student:
#     courses= ['History','maths']
#     def __init__(self, name: str, age:int): #must values
#         self.name = name
#         self.age = age
# s1= Student("John", 25)
# print(s1.__dict__)
# print(s1.courses)
#
# print(dir(Student))


# class Circle:
#     pi = 3.14
#     def __init__(self,r: float | int):
#         self.radius = r
#     def calculate_area(self):
#         return self.pi * self.radius**2
#     def calculate_perimeter(self):
#         return 2 * self.pi * self.radius
# c1=Circle(r=1.02)
# print(c1.calculate_area())
# print(c1.calculate_perimeter())

# class Department:
#     # class attribute
#     departmant_name = ''
#     employee_count = 0
#
#     def __init__(self, name: str, age: int):
#         # object attribute
#         self.name = name
#         self.age = age
#         Department.employee_count += 1
#
#     def show_info(self):
#         print(
#             f'Name: {self.name}\n'
#             f'Age: {self.age}\n'
#             f'Depermant Name. {self.departmant_name}'
#         )
#
#     def show_employee_count(self):
#         print(f'Total Employee: {self.employee_count}')
#
# d1 = Department(name='burak', age=36)
# d1.departmant_name = 'ARGE'
# d1.show_info()
# d1.show_employee_count()
#
# d2 = Department(name='hakan', age=39)
# d2.departmant_name = 'Amele'
# d2.show_info()
# d2.show_employee_count()
#
# d3 = Department(name='ipek', age=42)
# d3.departmant_name = 'qwe'
# d3.show_info()
# d3.show_employee_count()

class SoftwareDeveloper:
    knowledge_languages = []
    def __init__(self, first_name: str,last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    def add_new_languages(self,input_languages:str):
        lst_language=input_languages.split(',')

        for item in lst_language:
            if item not in self.knowledge_languages:
                self.knowledge_languages.append(item)
        return 'languages added'
    def show_info(self):
        return {
            f'First Name: {self.first_name}'
            f'Last Name: {self.last_name}'
            f'Knowledge Languages: {self.knowledge_languages}'
        }

s1 = SoftwareDeveloper(first_name='John',last_name='Smith')
print(
    s1.add_new_languages(input_languages='Python,c#,vb.net'))

print(
        s1.show_info()
)
