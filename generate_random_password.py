# code to generate some password

import random

length_password = int(input("Masukkan panjang password yang ingin dibuat: "))

key_password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*<>,>.?/:;"

make_password = "".join(random.sample(key_password, length_password))

print("The result of the password created: ", make_password)
