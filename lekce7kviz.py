from datetime import datetime, timedelta
zacatek_lekce = "07.11.2024, 18:00"
zacatek_lekce = datetime.strptime(zacatek_lekce, "%d.%m.%Y, %H:%M")
print(zacatek_lekce)


def time_to_christmas():
    return datetime (2024,12,24,18,0) - datetime.now()
print(time_to_christmas())
