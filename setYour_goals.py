import datetime

user_input = input(
    "Masukkan tujuan dan deadline Anda (Pisahkan antara keduanya dengan comma): ")
input_list = user_input.split(",")

if len(input_list) != 2:
    print("Format input tidak valid. Gunakan format: tujuan,dd.mm.yyyy")
else:
    goal = input_list[0].strip()
    deadline_str = input_list[1].strip()

    try:
        deadline = datetime.datetime.strptime(deadline_str, "%d.%m.%Y").date()
        today = datetime.date.today()

        sisa_hari = (deadline - today).days

        print(
            f"Sisa waktu tujuan '{goal}' tersisa: {sisa_hari} hari lagi")
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format: dd.mm.yyyy")

