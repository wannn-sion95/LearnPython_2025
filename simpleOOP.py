#ANAK JURUSAN TEKNIK TELEKOMUNIKASI
print("------------------------------------------")
print("Biodata ANAK JURUSAN TEKNIK TELEKOMUNIKASI")
print("------------------------------------------")
class telkomC:
    def __init__(self, nama, nrp, alamat):
        self.nama = nama
        self.nrp = nrp
        self.alamat = alamat

    def biodata(self):
        return f"Nama: {self.nama}\nNRP: {self.nrp}\nAlamat: {self.alamat}\n"

data = telkomC("Wannn Sion", 2224600080, "Mandailing Natal")
data2 = telkomC("Mhd. Ridwan", 2224600080, "Panyabungan Tonga")

print(data.biodata())
print(data2.biodata())


#ANAK JURUSAN TEKNIK INFORMATIKA
print("---------------------------------------")
print("Biodata ANAK JURUSAN TEKNIK INFORMATIKA")
print("---------------------------------------")
class ITB:
    def __init__(self, nama, nrp, alamat):
        self.nama = nama
        self.nrp = nrp
        self.alamat = alamat

    def biodata2(self):
        return f"Nama: {self.nama}\nNRP: {self.nrp}\nAlamat: {self.alamat}\n"

data3 = ITB("Ridwan Nasution", 3212400056, "Jakarta Barat")
data4 = ITB("Wannn Sion", 3212400052, "Mandailing Natal")

print(data3.biodata2())
print(data4.biodata2())
    
