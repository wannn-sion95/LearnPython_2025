number = int(input("Enter a number: "))
num = 0

while num < number:
    # Pola bintang menurun
    n = 0
    while n < number - num:
        print("*", end=' ')
        n += 1

    # Spasi sebagai pemisah
    print("  ", end='')  # 4 spasi

    # Pola bintang menaik
    n = 0
    while n < num + 1:
        print("*", end=' ')
        n += 1

    # Pindah ke baris berikutnya
    print()
    num += 1
