masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in masini1:
#     print(f'Masina mea preferata este FOR {i}')
#
# for masina in masini1:
#     print(f'Masina mea preferata este FOR EACH {masina}')
#
# i = 0
# while i < len(masini1):
#     print(f'Masina mea preferata este WHILE {masini1[i]}')
#     i = i + 1

# masini2 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# prima_masina = masini2[0]
# print(prima_masina)
# ultima_masina = masini2[len(masini2) - 1]
# print(ultima_masina)
# for masina in range(1, len(masini2) - 1):  # ne deplasam de la a doua poz pana la penultima
#     masini2[masina] = masini2[masina].upper()  # facem pentru toate aceste elemente litere mari
# else:
#     print(masini2)  # printam lista modificata

# for masina in masini1:
#     if masina == 'Mercedes':
#         print('AM GASIT MASINA DORITA')
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam')


# for masina in masini1:
#     if masina == 'Trabant':
#         continue
#     elif masina == 'Lastun':
#         continue
#     else:
#         print(f'S-ar putea sa va placa {masina}')

# masini_vechi = []
# masina1 = 'Lastun'
# masina2 = 'Trabant'
# masina3 = 'Tesla'
# for i in range(0, len(masini1)):
#     if masini1[i] == masina1 or masini1[i] == masina2:
#         masini_vechi.append(masini1[i])
#         masini1[i] = masina3
# print(f'Modele noi{masini1}')
# print(f'Modele vechi{masini_vechi}')

# pret_masini = {
#     'Dacia': '6800',
#     'Lastun': '500',
#     'Opel': '1100',
#     'Audi': '19000',
#     'BMW': '23000'
# }
# buget = 29000
# itemi = pret_masini.items()
# print(itemi)
# for iteme in itemi:
#     pret_masina = iteme[1]
#     if buget >= int(pret_masina):
#         print(f'Pentru bugetul actual de {buget} puteti cumpara {iteme[0]} care costa {iteme[1]}')
#     else:
#         print(f'{iteme[0]} e prea scumpa pentru bugetul d-voastra de {buget} pentru ca are pretul de {iteme[1]}')

# y = 0
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3, 3, 3, 3, 3, 0]
# for i in numere:
#     if i == 3:
#         y = y + 1
# print(f'numarul apare de {y} ori')

# suma = 0
# numere = [1, 2, 1, 1, 1, 3, 1, 11, -4, 3]
# for i in numere:
#     suma = suma + i
# print(f'Suma este {suma}')


# numere = [1, 1, 3, 1, 3, 3, 1, 11, -4, 99]
# maxim = 2
# for i in numere:
#     if i > maxim:
#         maxim = i
# print(f'Maxim este {maxim}')


numere = [5, 7, 3, 9, 3, 3, 1, 11, -4, 3]
# for i in range(len(numere)):
#     if int(numere[i]) > 0:
#         numere[i] = - numere[i]
# print(numere)

# for x in numere:
#     print(-x)


# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []

# for i in alte_numere:
#     if i > 0:
#         numere_pozitive.append(i)
#     else:
#         numere_negative.append(i)
#     if i % 2 == 0:
#         numere_pare.append(i)
#     else:
#         numere_impare.append(i)
# print(numere_pozitive)
# print(numere_pare)
# print(numere_impare)
# print(numere_negative)



# import random
# numar_ghicit = []
# numar = int(input('Alege un numar: '))
# numar_secret = random.randint(1, 5)
# print(numar_secret)
# while numar < numar_secret:
#     print('Numarul secret e mai mare')
#     break
# if numar > numar_secret:
#     print('Numarul secret este mai mic.')
# elif numar == numar_secret:
#     print('Felicitari! Ai ghicit!')

# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# for x in tastatura_telefon:
#     for y in x:
#         print(f'Cifra curenta este', y)
#         #nested  = cuib


