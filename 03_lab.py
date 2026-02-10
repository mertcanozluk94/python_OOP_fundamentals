# season = input('lutfen mevsimi gir:').lower()

# if season == "kis":
#     print("kis aylari")
# elif season == "yaz":
#     print("yaz aylari")
# elif season == "sonbahar":
#     print("sonbahar aylari")
# elif season == 'ilkbahar':
#     print("ilkbahar aylari")
# else:
#     print("hicbiri yok")

# isim = input ('ismi giriniz:')
# parola = input('parolayi gir:')

# if isim == 'kerem' and parola == 'mrv123':
#     print(f'{isim} giris basarili')
#     boy = float(input('boyu gir:'))
#     kilo = float(input('kiloyu gir:'))
#     bmi = kilo / (boy *2)
#     sonuc = None
    
#     if bmi > 0 and bmi < 20:
#         sonuc = "1"
#     elif bmi <20.1 and bmi >40:
#         sonuc = '2'
#     elif bmi <40.1 and bmi >60:
#         sonuc = '3'
#     print(f'kullanici: {isim}'
#           f' bmi: {bmi}'
#           f' sonuc: {sonuc}')

# else:
#     print('oyle user yok')

# # Nested If
# vehicle = input('Vehicle: ').lower()
# speed = float(input('Speed: '))
#
# if speed > 0:
#     if vehicle == 'car':
#         if speed >= 60:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     elif vehicle == 'truck':
#         if speed >= 40:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     elif vehicle == 'motorcycle':
#         if speed >= 70:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     else:
#         print('Please type a proper vehicle type..!')
# else:
#     print('Invalid speed value..!')

# mevsim = input('mevsimi gir:').lower()
# match mevsim:
#     case 'kis':
#         print('kis mevsimleri')
#     case 'yaz':
#         print('yaz mevsimleri')
#     case 'ilkbahar':
#         print('ilkbahari mevsimleri')
#     case 'sonbahar':
#         print('sonbahari mevsimleri')
#     case _:
#         print('hicbiri yok')
# hatalı kodu ignore edip yoluna devam eder try/except/finally asagidaki ornekte 0 a bolunme var
# try:
#     bolen = int (input('bolen:'))
#     bolunen = int(input('bolunen:'))
#     sonuc = bolunen / bolen
#     print(f'Sonuc: {sonuc}')
# except ZeroDivisionError as err:
#     print(err)
# finally:
#     print('baglanti kopariliyor')

try:
    age = int(input('yas:'))
    print(f'yas: {yas}')
except ValueError as err:
    print('yas bilgisi harf icermez')
except ZeroDivisionError as err:
    print (err)
except:
    print('python icerisinde built in olan tüm exceptionlara bakar')
else:
    print('except tetiklenmezse else calisir')