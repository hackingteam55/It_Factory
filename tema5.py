# def sumaa(a, b):
#     #print(a + b)
#     return a + b
#
#
# print(sumaa(3, 9))
#
#
#
# def par_impar():
#     x = int(input('Introdu x'))
#     if x % 2 == 0:
#         print('x este numar par')
#     else:
#         print('x este numar impar')
#
#
# par_impar()


# def caractere():
#     x = input('Introdu nume')
#     print(len(x)) # grija la len
#     y = input('Introdu prenume')
#     print(len(y)) # grija la len
#     if len(x) and len(y) != 0:
#         print(f'Numele tau are {(len(x) - 1) + (len(y) - 1)} caractere')
#     else:
#         print('Nu ai introdus nume sau prenume')
#
#
# caractere()

# def arie_dreptunghi():
#     lung = int(input('introduceti lungimea dreptunghiului: '))
#     lat = int(input('introduceti latimea dreptunghiului: '))
#     if lung and lat != 0:
#         return(f'Aria dreptunghiului este {(lung * lat)}')
#
#
# print(arie_dreptunghi())

# import math
#
#
# def arie_cerc():
#     x = int(input('Introdu lungimea razei cercului: '))
#     if x != 0:
#         return(f'Raza cercului este {(x * x) * math.pi }')
#
#
# print(arie_cerc())

# def caracters():
"""
x: (String) - user input from keyboard - stringul in care cautam caracterul dorit
y: (String) - user input from keyboard - caracterul dorit
"""

#     x = input('Introduceti un string: ')
#     y = input('Introduceti caracterul dorit: ')
#     if x and y:
#         if y in x:
#             return(f'Caracterul "{y}" se gasete in string-ul "{x}"')
#         else:
#             return(f'Nu gasim caracterul "{y}" in string-ul "{x}"')
#
#
# print(caracters())

# def upper_lower():
#     x = input('String-ul este: ')
#     count_mare = 0
#     count_mic = 0
#     for let in x:
#         if let == " ":
#             continue
#         elif let.isupper():
#             count_mare = count_mare + 1
#         else:
#             count_mic = count_mic + 1
#     print(f'Numarul de litere mici este {count_mic}')
#     print(f'Numarul de litere mari este {count_mare}')
#
#
# upper_lower()

# def lista():
#     x = input('Introduceti lita: ')
#     x2 = []
#     for y in x:
#         if y == ',':
#             continue
#         elif y == '-':
#             x2 = x2.append(abs(int(y)))
#             print(x2)
#         else:
#             return x
#
#
# print(lista())

# x = [2, 3, 4, -3, -867548, -45, -45.789, 23.5, 765.0]
#
#
# def lista_nr(lista):
#     lista_nrpozitive = []
#     for a in lista:
#         if a > 0:
#             lista_nrpozitive.append(a)
#     return lista_nrpozitive
#
#
# raspuns = lista_nr(x)
# print(f'Numerele pozitive din lista sunt: {raspuns}!')

# x = input('Introduceti un numar: ')
# y = input('Introduceti un numar: ')
#
#
# def numere(nr1, nr2):
#     if nr1 > nr2:
#         print('Primul nr mai mare decat al doilea numar')
#     elif nr2 > nr1:
#         print('Al doilea nr este mai mare decat primul nr')
#     else:
#         print('Numerele sunt egale')
#
#
# numere(x, y)

#set_numere={1, 2, 3, 4, 5, 6, 7, 8}


# def functie_numar(n1, numere):
#     if n1 in numere:
#         print('Nu am adaugat numarul in set. Acesta exista deja')
#         return False
#     else:
#         numere.add(n1)
#         print('Am adaugat numarul nou in set!')
#         return True
#
#
# print(functie_numar(8, set_numere))
# print(f'Setul este = {set_numere}')


# def zile_luna(luna):
#     luni_28 = ['Februarie']
#     luni_30 = ['Aprilie', 'Iunie', 'Septembrie', 'Noiembrie']
#     luni_31 = ['Ianuarie', 'Martie', 'Mai', 'Iulie', 'August', 'Octombrie', 'Decembrie']
#     if luna in luni_28:
#         return 28
#     elif luna in luni_30:
#         return 30
#     elif luna in luni_31:
#         return 31
#
#
# lunatastatura = input('Introdu luna : ')
# print(zile_luna(lunatastatura))




