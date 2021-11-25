import colorsys

print("Dla RGB podaj liczbę całkowitą z przedziału <0;255>")

R=int(input("Wartość Red: "))
G=int(input("Wartość Green: "))
B=int(input("Wartość Blue: "))

hsv=list(colorsys.rgb_to_hsv(R/255,G/255,B/255))
