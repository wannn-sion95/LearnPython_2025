from datetime import datetime

user_input = input("Masukkan tujuan anda dengan batas waktu: ")
input_list = user_input.split(",")

goal = input_list[0]
deadline = input_list[1]

deadline = datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.today()

sisa_hari = deadline - today
sisa_jam = int(sisa_hari.total_seconds() / 60 / 60)

print(f"Sisa waktu untuk mencapai {goal} tersisa: {sisa_jam} jam")
