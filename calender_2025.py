import calendar
from rich.console import Console
from rich.table import Table

def colorful_calendar(year):
    console = Console()
    months = [calendar.monthcalendar(year, month) for month in range(1, 13)]

    for month in range(12):
        month_name = calendar.month_name[month + 1]

        table = Table(title=f"[bold cyan]Bulan {month_name} \
        Tahun  {year} [/bold cyan]", show_lines=True)

        table.add_column("Sen", justify="center", style="white")
        table.add_column("Sel", justify="center", style="white")
        table.add_column("Rab", justify="center", style="white")
        table.add_column("Kam", justify="center", style="white")
        table.add_column("Jum", justify="center", style="white")
        table.add_column("Sab", justify="center", style="red")
        table.add_column("Ming", justify="center", style="red")

        for week in months[month]:
            table.add_row(*[str(day) if day != 0 else "" for day in week])

            console.print(table)
            console.print("\n")
if __name__ == "__main__":
    colorful_calendar(2025)
