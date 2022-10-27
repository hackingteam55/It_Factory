note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

#1
print(note_muzicale)
print(note_muzicale[::-1])
note2 = note_muzicale[::-1]
note2.reverse()
print(note2)
#2
print(note2.count('do'))

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
l3 = l1 + l2
#3
print(l3)
l1.extend(l2)
print(l1)

#4
l1.sort()
print(l1)
l1.pop(0)
print(l1)

#5
if len(l1) == 0:
    print('lista goala')
else:
    print(f'lista are {len(l1)} elemente')

#6
#del l1

#7

if len(l1) != 0:
    print('lista goala')
else:
    print(f'lista are {len(l1)} elemente')

#8
dic = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
elevi = dic.keys()
print(elevi)

#9



