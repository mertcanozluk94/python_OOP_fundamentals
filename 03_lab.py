user = input ('enter name:')
password = input('enter pass:')

if user == 'kerem' and password == 'mrv123':
     print(f'{user} giris basarili')
     height = float(input('enter height:'))
     weight = float(input('enter weight:'))
     bmi = weight / (height *2)
     result = None
    
     if bmi > 0 and bmi < 20:
         result = "1"
     elif bmi <20.1 and bmi >40:
         result = '2'
     elif bmi <40.1 and bmi >60:
         result = '3'
     print(f'user: {user}'
           f' bmi: {bmi}'
           f' result: {result}')

else:
     print('no user')

#Nested If
vehicle = input('Vehicle: ').lower()
speed = float(input('Speed: '))

if speed > 0:
     if vehicle == 'car':
         if speed >= 60:
             print('Penalty..!')
         else:
             print('No penalty..!')
     elif vehicle == 'truck':
         if speed >= 40:
             print('Penalty..!')
         else:
             print('No penalty..!')
     elif vehicle == 'motorcycle':
         if speed >= 70:
             print('Penalty..!')
         else:
             print('No penalty..!')
     else:
         print('Please type a proper vehicle type..!')
else:
     print('Invalid speed value..!')

season = input('enter season:').lower()
match season:
     case 'winter':
         print('winter season')
     case 'summer':
         print('summer season')
     case 'spring':
         print('spring season')
     case 'autumn':
         print('autumn season')
     case _:
         print('none of season')
#It ignores the faulty code and continues with try/except/finally. In the following example, there is a division by 0.
try:
     dividing = int (input('dividing:'))
     divided = int(input('divided:'))
     result = divided / dividing
     print(f'result: {result}')
except ZeroDivisionError as err:
     print(err)
finally:
     print('no connection')

try:
    age = int(input('age:'))
    print(f'age: {age}')
except ValueError as err:
    print('doesnt contain letters')
except ZeroDivisionError as err:
    print (err)
except:
    print('Python checks for all built-in exceptions.')
else:
    print('It works unless the exception trigger is activated.')
