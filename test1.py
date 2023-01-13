# #b.10     -demonstrati cu assert ca stringul nu contine doar numere
# coral = 'Coral is either the stupidest animal or the smartest rock'
# a = coral.isdigit()
# print(a)
#
# coral_num = '1234123412341234123'
# b = coral_num.isdigit()
# print(b)
#
# print('hy')
# assert a == 0
# print('Eroare de asertie')
#Primesc eroare si nu stiu de ce?
#c.18.
# var = 'alabala portocala'
# lista = var.split()
# print(lista)
# primul = var[0]
# print(primul)
# litera_mare = var[1:-1].replace('a', 'A')
# print(primul + litera_mare + primul)
#
# import math
# string_impar = input("Introduceti un string impar ")
# x = string_impar[math.floor(len(string_impar) / 2)]
# print(x)
# import calendar
# a = 17
# b = 5
#
# a += b
# print(a)

# a = 0
# b = 5
# c = (a & b) | (a & a) | (a | b)
# print("c")

# fruits = {'mango', 'peach', 'grape', 'potato'}
# fruits.add('mango')
# fruits.add('kiwi')
# print(fruits)

# seta = {1,2,3,4,5}
# setb = {1,2,3,4,5,6,7}
# assert seta < setb

# vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(vals[::-1][2:5])

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # assert data[1] == data[3]
#
# data.insert(-1, 10)
#
# print(data)
#
# data.append(20)
#
# print(data)
#
# data.pop()
#
# print(data)
#
# data.pop(2)
#
# print(data)
#
# data.extend([6, 7])
# print(data)
#
# num1 = 15
# num2 = 20
# res = num1 & num2
#
# print(res)

# num1 = 15
# num2 = 20
# res = not(num1 & num2)
# print(res)

# list = ['Apple', 'Mango', 'Grapes', 1, 2, [1, 2, 3], True, 3.0]
#
# print(list[1:5])

# def print_nume(nume, prenume):
#     mesaj = (f'hi {nume} {prenume}')
#     return mesaj
#
# print(print_nume('Ion', 'test'))


# from calendar import monthrange
#
# num_days = monthrange(2022, 11)[1]
# print(num_days) # aici se printeaza numarul de zile
#
# def nr_zile():
#     return monthrange(2021, 11)
# print(nr_zile())

# from calendar import monthrange
# def numar_zile_ale_lunii(an=2022,luna=2):
#     return monthrange(2022, 1)
# print(numar_zile_ale_lunii(2022,2))

