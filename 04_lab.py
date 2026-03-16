#Loops
# counter = 0
# while counter < 10:
#     print(counter)
#     counter = (counter + 1)
#
# counter1 = 9
# while counter1 >=0:
#     print(counter1)
#     counter1 = (counter1 -1)

# counter2 = 0
# while counter2 <= 100:
#     print(counter2 , end= ",")
#     counter2 = (counter2 +1)

#sum of odd and even numbers
# counter= 0
# odd_sum=0
# even_sum=0
# counter = counter + 1
#
# while counter <=100:
#     if counter %2 == 0:
#         even_sum = even_sum + counter
#     else:
#         odd_sum = odd_sum + counter
# print (f'odd sum: {odd_sum} , even sum: {even_sum}')

# while True:
#     try:
#         process = input('process: ')
#         if process == 'e':
#             break #loop finishes
#     except ZeroDivisionError as err:
#         print(err)
#     except ValueError as err:
#         print(err)

#prime number calculate

# number= int(input('enter number:'))
# if number < 2:
#     print('number less than 2 you cant control prime')
# else:
#     is_prime = True
#     count = 2
#     count = +1
#     while count < number:
#         if number % count == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print('number is prime')
#     else:
#         print('number is not prime')

# number = int(input("Enter a number: "))
# if number < 0:
#     print('you cannot calculate')
# elif  number == 1 or number == 0:
#         print('answer 1')
# else:
#         answer = 1
#
#         while number > 0:
#             answer *= number
#             number -= 1
#         print(f'answer {answer}')