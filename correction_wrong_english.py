from textblob import TextBlob

title = "-------------------------------------------------\nMengkoreksi Kalimat Yang Salah Dan Memperbaikinya\ndalam bahasa inggris\n-------------------------------------------------"
print(title)


def convert(string):
    li = list(string.split())
    return li


input_kalimat = input("Masukkan kalimat: ")
kalimat = convert(input_kalimat)
kalimat_benar = []
for i in kalimat:
    kalimat_benar.append(TextBlob(i))

print("Kalimat yang salah: ", kalimat)
print("Kalimat yang sudah diperbaiki: ")
for i in kalimat_benar:
    print(i.correct(), end=' ')
