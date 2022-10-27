class Cerc:
    raza: None
    culoare: None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie(self, raza, culoare):
        if raza:
            x = input('Introdu raza')
            print(f'Raza cercului este egala cu {x}')
        else:
            print('Nu am gasit raza')
        if culoare:
            print(f'Culoarea este {culoare}')
        else:
            print('Nu ati introdus culoarea')

    def aria(self):
        pi = 3.14
        raza = int(input('Introdu raza '))
        if raza:
            return raza ** raza * pi
        else:
            return 'Nu ai introdus raza'

    def diametru(self):
        raza = int(input('Introdu raza '))
        if raza:
            return 2 * raza
        else:
            return 'Nu ai introdus raza'

    def circumeferinta(self):
        pi = 3.14
        raza = int(input('Introdu raza '))
        if raza:
            return 2 * pi * raza
        else:
            return 'Nu ai introdus raza'


cerc = Cerc(23, 'rosu')

cerc.descrie(45, 'galben')
print('Diametru este', cerc.diametru())
print('Circumferinta este', cerc.aria())

