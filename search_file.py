nama_file = input("Masukkan nama file yang ingin dicari: ")

try:
    with open(nama_file, 'r') as file:
        for baris in file:
            print(baris.strip())
except FileNotFoundError:
    print("File tidak ditemukan!")
