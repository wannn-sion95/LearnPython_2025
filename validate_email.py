import re

print("INFO: email tidak boleh menggunakan spasi")

email_valid = input("Masukkan nama email: ")
input_benar = re.match(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email_valid)

if input_benar:
    print(email_valid, "\nEmail yang anda masukkan cocok dengan sistem")

else:
    print(email_valid, "\nEmail yang anda masukkan tidak cocok dengan sistem")
