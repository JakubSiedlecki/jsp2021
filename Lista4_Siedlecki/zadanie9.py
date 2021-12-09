import math


n = int(input("Podaj liczbę, z której program ma obliczyć silnię: "))

#if n < 0:
#    print("Silnia dla liczby ujemnej nie istnieje w zbiorze liczb całkowitych")

if n < 0:
    print("Nie istnieje silnia z liczb ujemnych")
elif n == 0:
    print("Silnia dla 0 wynosi 1")
elif n>0:
    s = math.factorial(n)
    print("Silnia dla podanej liczby wynosi: ",s)