class Cewek_idaman:
    def nama(self):
        return "Daftar cewek yang gw suka: "

class Jihyo(Cewek_idaman):
    def nama(self):
        return "Jihyo"

class Rayna(Cewek_idaman):
    def nama(self):
        return "Rayna"

class Anita(Cewek_idaman):
    def nama(self):
        return "Anita"

idaman = [Cewek_idaman(), Jihyo(), Rayna(), Anita()]
                                                      
for Cewek_idaman in idaman:

    print(Cewek_idaman.nama())
