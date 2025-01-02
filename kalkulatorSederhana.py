from prettytable import PrettyTable

print("Kalkulator Sederhana")
print("---------------------")
angka_pertama = input("Masukkan angka pertama: ")
angka_kedua = input("Masukkan angka kedua: ")

print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan_operasi = input("Masukkan pilihan operasi (1-4): ")

try:
    angka_pertama = int(angka_pertama)
    angka_kedua = int(angka_kedua)
    
    if pilihan_operasi == "1":
        hasil = angka_pertama + angka_kedua
        operasi = "Penjumlahan"
    elif pilihan_operasi == "2":
        hasil = angka_pertama - angka_kedua
        operasi = "Pengurangan"
    elif pilihan_operasi == "3":
        hasil = angka_pertama * angka_kedua
        operasi = "Perkalian"
    elif pilihan_operasi == "4":
        hasil = angka_pertama / angka_kedua
        operasi = "Pembagian"
    else:
        print("Operasi tidak dikenali")
        exit()

    # Membuat tabel untuk menampilkan hasil
    table = PrettyTable()
    table.field_names = ["Operasi", "Angka Pertama", "Angka Kedua", "Hasil"]
    table.add_row([operasi, angka_pertama, angka_kedua, hasil])
    print(table)

except ValueError:
    print("Input harus berupa angka.")
except ZeroDivisionError:
    print("Pembagian dengan nol tidak valid.")
