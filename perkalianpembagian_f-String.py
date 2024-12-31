print("Perkalian dan Pembagian")
print("--------------------------------")
angkaPertama = int(input("Masukkan angka pertama yang ingin anda kali dan bagi: "))
angkaKedua = int(input("Masukkan angka kedua yang ingin anda kali dan bagi: "))

hasilPerkalian = f"Hasil Perkalian dari {angkaPertama} x {angkaKedua} = {angkaPertama * angkaKedua}"

try:
    hasilPembagian = f"Hasil Pembagian dari {angkaPertama} : {angkaKedua} = {angkaPertama / angkaKedua}"
except ZeroDivisionError:
    hasilPembagian = "Pembagian dengan nol tidak berlaku karena hasilnya akan tetap nol."

print(hasilPerkalian)
print(hasilPembagian)
