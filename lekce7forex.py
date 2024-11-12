from forex_python.bitcoin import BtcConverter

b = BtcConverter()
print(b.get_latest_price("USD"))

# pro odinstalování balíčku pip3 uninstall forex-python
# další balíčky https://dev.to/taipy/top-42-python-libraries-you-need-to-know-1omo

from faker import Faker

fake = Faker()

print(fake.name())
print(fake.address())
print(fake.text())

for _ in range(10):
    print(fake.name())


from faker import Faker

# Vytvoření instance Faker s českou lokalizací
fake = Faker("cs_CZ")

# Generování náhodného ženského jména
print(fake.first_name_female())

# Generování náhodné adresy
print(fake.address())

# Generování náhodného textu
print(fake.text())

# Generování 10 náhodných ženských jmen
for _ in range(10):
    print(fake.first_name_female())

# Generování 10 náhodných adres
for _ in range(10):
    print(fake.address())


cislo = 1
if cislo % 2 == 1:
    print("Číslo je liché")
