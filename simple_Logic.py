lanjut = True

while lanjut:
    angka = int(
        input("Masukkan angka yang harus lebih besar dari 0 atau angka genap: "))

    if angka <= 0 or angka % 2 == 1:
        print("Angka:", angka, "tidak sesuai yang diinginkan")
        print("Silahkan coba lagi")
    else:
        print("Angka yang anda masukkan:", angka,
              "merupakan angka yang sesuai")
        lanjut = False
        print("Program berhasil")
