print("================================================")
print("Selamat Datang di Program Data Mahasiswa Telkom")
print("================================================")
class mahasiswa_telkom:
    def __init__(self, nama, nim, alamat):
        self.nama =  nama
        self.nim = nim
        self.alamat = alamat

class Anita(mahasiswa_telkom):
    def data_mahasiswa(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nAlamat: {self.alamat}\n"

class alex(mahasiswa_telkom):
    def data_mahasiswa(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nAlamat: {self.alamat}\n"

class syakira(mahasiswa_telkom):
    def data_mahasiswa(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nAlamat: {self.alamat}\n"

class rania(mahasiswa_telkom):
    def data_mahasiswa(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nAlamat: {self.alamat}\n"

class wannn(mahasiswa_telkom):
    def data_mahasiswa(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nAlamat: {self.alamat}\n"

class putri(mahasiswa_telkom):
    def data_mahasiswa(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nAlamat: {self.alamat}\n"

nita = Anita("Anita Rahmadani", 242560045, "Bandung")
lex = alex("Alex Fernando", 242560046, "Jakarta")
kira = syakira("Syakira Putri", 242560047, "Malang")
rani = rania("Rania Kayla", 242560048, "Surabaya")
wann = wannn("Mhd. Ridwan", 242560049, "Panyabungan")
puput = putri("Putri Khairani", 242560050, "Semarang")

print(nita.data_mahasiswa())
print(lex.data_mahasiswa())
print(kira.data_mahasiswa())
print(rani.data_mahasiswa())
print(wann.data_mahasiswa())
print(puput.data_mahasiswa())
