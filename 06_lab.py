liste = ['lambo','ferro','velo']
 print(liste[2])
liste.append('kero')
 print(liste)

liste.remove("ferro")
 print(liste)

liste.pop(0)
 print(liste)

try:
     liste.pop(25)
     print(liste)
except IndexError as err:
     print(err)

for listes in liste:
     print(listes)

word= input('enter alphabet:').lower()
 list1=['a','e','i','u','o']
 list2=[]
 list3=[]

for c in word:
     if c.isalpha():
         if c not in list2 and c not in list3:
             if c in list1:
                 list2.append(c)
             else:
                 list3.append(c)
 print(f'list2: {list2} , list3: {list3}')
 import string

users = ["kerem bastro","ozgur gevsek","selim mali kesin","murat guloglu"]

mail_address= []
for user in users:
     user_names= user.split(' ')
     for item in user_names:
         if item == ' ':
             user_names.remove(item)
         if user == ' ':
             continue
         elif len(user_names) >= 2:
             mail_addres=f'{user_names[0]}.{user_names[-1]}@outlook.com'
             mail_address.append(mail_addres)
 print(mail_address)

from random import randint
 list1 = []
 list2 = []
for i in range(10):

     list1.append(randint(0, 100))
     list2.append(randint(0, 100))
     random_num=randint(0,10)
     print(random_num)
     print(f'{list1},{list2}')

from string import punctuation
 password= input("enter your password: ")
 if len(password) < 16:
     print("password is too short")
 for c in password:
     if not c.isupper() or not c.islower() or not c.isdigit() or not c in punctuation:
         print(c)
from random import randint
lst=[]
for a in range(10):
    random_number = randint(0,100)
    lst.append(random_number)
print(lst)

print([randint(a=0,b=100) for a in range(10)])

print([i for i in range(101) if i%2==0])
