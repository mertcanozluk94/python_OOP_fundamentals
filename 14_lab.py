# #I/O
# #mode: r,w,a
# from os import write
#
# try:
#     file = open(file='iofile.txt',mode='w',encoding='utf-8')
#     file.write('Full name: krm \n occ: doctor\n')
#     file.close()
# except FileExistsError as err:
#     print(err)
# except NameError as err:
#     print(err)

from socket import gethostname,gethostbyname
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def sys_log(**kwargs) -> str:
    try:
        if '@' not in kwargs.get('email_address:'):
            raise ValueError('invalid email address')
        return 'your mail correct'
    except ValueError as err:
        aes_key = get_random_bytes(16)
        aes_obj = AES.new(key=aes_key,mode=AES.MODE_ECB)
        chipper_text = aes_obj.encrypt(kwargs.get('ip_address'))
        with open(file=kwargs.get('file'),mode='a',encoding='utf-8') as file:
            file.write(str(chipper_text))
            file.write(' || ')
            file.write(f'Machine Name: {kwargs.get('machine_name')}')
            file.write(' || ')
            file.write(f'IP Address: {kwargs.get('ip_address')}')
            file.write(' || ')
            file.write(f'Exception Date: {kwargs.get('exception_date')}')
            file.write(' || ')
            file.write(f'Email Address: {kwargs.get('email_address')}')
            file.write(' || ')
        return f'{err}'


print(
    sys_log(
        file='log.txt',
        machine_name=gethostname(),
        ip_address=gethostbyname(gethostname()),
        exception_date=datetime.now(),
        email_address='krm.krm.com'

    )
)