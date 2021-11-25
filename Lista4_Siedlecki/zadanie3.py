import math

print("Program zamienia stopnie na radiany lub radiany na stopnie.")
x = int(input("1 - stopnie na radiany, 2 - radiny na stopnie.\n"))
a = float(input("Podaj wymiar kąta: "))

if x==1:
    A = a*((math.pi)/180)
    print("Wymiar kąta a w radianach: ")
    print(A)
if x==2:
    B = a*(180/(math.pi))
    print("Wymiar kąta a w stopniach: ")
    print(B)
