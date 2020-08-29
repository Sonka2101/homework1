import random

chars = '012345uewuwoirjeiwuruwi54683959048Y489jroieury78o2349u9498yruieiikj4283wujuiy39jr9eijrh78w36789'

number = int(input('Ծածկագրերի քանակը․'))
lenght = int(input('Տողի երկարությունը․'))

for user_name in range(number):
    password = ''

    for per_user in range(lenght):
        password += random.choice(chars)

    print(password)

    file = open('password.txt', 'a')
    file.write('\n' + password)
    file.close()