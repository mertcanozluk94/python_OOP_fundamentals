m= float(input('kerem:'))
print(type(m))

area = m*m
premiter = 4*m

print("area:",area)
print("premiter:",premiter)
print(f'area: {area} - \n premiter: {premiter}')
print(f'area: {area,premiter}')

#F5 debug - F11 step step

a = int(input('number:'))
b = int(input('number:'))

if a > b:
    print(f'{a} bigger')
else: #all of other condiions
    print(f'{b} bigger')

x= int (input('number:'))

result= x % 2

if result == 0:
    print(f'{x} even')
else:
    print(f'{x} odd')

season = input('enter season:').lower

if season == "winter":
    print("winter season")
elif season == "summer":
    print("summer season")
elif season == "spring":
    print("spring season")
elif season == "autumn":
    print("autumn season")
else:
    print("none season")