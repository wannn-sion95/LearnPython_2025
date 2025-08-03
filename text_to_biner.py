def teks_biner(teks):
    hasil = ""
    for huruf in teks:
        biner = format(ord(huruf), '08b')
        hasil += biner + " "
    return hasil


teks = "Hai Renata"
print("Angka biner: ", teks_biner(teks))
