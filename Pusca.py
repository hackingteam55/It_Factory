class Pusca():
    model = None
    culoare = None
    gloante = None
    piedica_pusa = True

    def __init__(self, culoare, model, piedica_pusa, gloante):
        self.culoare = culoare
        self.model = model
        self.piedica_pusa = piedica_pusa
        self.gloante = gloante

    def descrie(self):
        print(f'{self.model} este o arma de culoarea {self.culoare}')

    def trage(self, piedica_pusa):
        if piedica_pusa:
            self.piedica_pusa = piedica_pusa
            print(f'Daca {self.model} are piedica pusa nu puteti trage')
        else:
            print(f'Puteti trage cu {self.model}')

    def incarca(self, gloante):
        if gloante == 0:
            self.gloante = gloante
            print(f'Trebuie sa incarci pentru ca ai {gloante} gloante')
        elif gloante < 5:
            self.gloante = gloante
            print(f'In curand o sa trebuiasca sa incarci pentru ca mai ai {gloante} gloante')
        else:
            print(f'Puteti trage linistiti')


pusc1 = Pusca('rosu', 'AK-47', True, 0)
pusc2 = Pusca('galben', 'PUSKSA', True, 4)
pusc3 = Pusca('verde', 'M16', True, 10)

pusc1.descrie()
pusc1.trage(True)
pusc1.incarca(0)

pusc2.descrie()
pusc2.trage(False)
pusc2.incarca(3)

pusc3.descrie()
pusc3.trage(False)
pusc3.incarca(6)

