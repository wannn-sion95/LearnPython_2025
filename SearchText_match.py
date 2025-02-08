import re

text = "Saya kuliah di Politeknik Elektronika Negeri Surabaya(PENS)!"
pattern = r"PENS"

match = re.search(pattern, text)

if match:
    print("Kata yang dicari ditemukan di indeks:", match.start())  
else:
    print("Kata yang ingin dicari tidak ditemukan.")
