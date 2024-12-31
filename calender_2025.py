import calendar

year = 2025
calendar.setfirstweekday(calendar.MONDAY)
week_number = 1

print(f"Kalender Tahun {year}\n")

for month in range(1, 13):
    print(f"\n{calendar.month_name[month]}")
    print("W    Sen   Sel   Rab   Kam   Jum   Sab   Min")

    month_cal = calendar.monthcalendar(year, month)

    for W in month_cal:
        week_with_week = [f"W{week_number:02d}"]
        week_with_week += [f"{day:2}" if day != 0 else "  " for day in W]
        print("   ".join(week_with_week))

        week_number += 1
