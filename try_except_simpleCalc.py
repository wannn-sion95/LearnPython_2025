print("--------------------")
print("Kalkulator Sederhana")
print("--------------------\n")

try:
  angka_pertama = float(input("Masukkan angka pertama: "))
  angka_kedua = float(input("Masukkan angka kedua: "))

  variabel_operasi = 1, 2, 3, 4

  pilih_operasi = print("\nOperasi Matematika\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian")

  input_operasi = int(input("Pilih operasi: "))
  if input_operasi not in variabel_operasi:
    print("Operasi tidak tersedia")

  if input_operasi == 1:
    print(f"Hasil dari pemjumlahan: {angka_pertama + angka_kedua}")
  elif input_operasi == 2:
    print(f"Hasil dari pengurangan: {angka_pertama - angka_kedua}")
  elif input_operasi == 3:
    print(f"Hasil dari perkalian: {angka_pertama * angka_kedua}")
  elif input_operasi == 4:
    print(f"Hasil dari pembagian: {angka_pertama / angka_kedua}")

except ValueError:
  print("Input harus berupa angka")

except ZeroDivisionError:
  print("Hasil tidak muncul karena 0 tidak bisa dibagi")
