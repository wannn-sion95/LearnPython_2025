#Belajar Polymorphism and method Overriding

class crush:
        def address(self):
                return "Alamat crush: "

class rania(crush):
        def address(self):
                return "Rania orang Bandung"

class rayna(crush):
        def address(self):
                return "Rayna orang Palembang"

class anita(crush):
        def address(self):
                return "Anita orang Mandailing"


def beutiful_woman(incaran):
        print(incaran.address(beutiful_woman))

rani = rania
ray = rayna
nita = anita


beutiful_woman(rania)
beutiful_woman(rayna)
beutiful_woman(anita)
