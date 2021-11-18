import re

print("Wymagania hasła: \n • Zawiera co najmniej 1 literę alfabety [a − z] oraz [A − Z]. \n • Zawiera co najmniej 1 licznę z przedziału [0 − 9]. \n • Zawiera co najmniej 1 znak specjalny ze zbioru [$#@] \n • Długość hasła jest nie mniejsza niż 6 znaków i nie dłuższa niż 16 znaków.")

password=input("Podaj hasło: ")

a = re.search("[a-z]", password)
b = re.search("[A-Z]", password)
c = re.search("[0-9]", password)
d = re.search("$,#,@", password)
e = len(password)>6 and len(password)<16

if (a and b and c and d and e):
    print("Hasło spełnia podane wymagania")
else:
    print("Hasło nie spełnia podanych wymagań")
