R = int(input("Podaj wartość R: "))
G = int(input("Podaj wartość G: "))
B = int(input("Podaj wartość B: "))

R = R/255
G = G/255
B = B/255

Cmax = max(R,G,B)    #max wartości R,G,B
Cmin = min(R,G,B)    #min wartości R,G,B
diff = Cmax-Cmin         

# jeśli Cmax = Cmin wtedy h = 0
if Cmax == Cmin:
    h = 0
# jeśli Cmax = R oblicz h tak samo dla Cmax = G,B
elif Cmax == R:
    h = (60*((G-B)/diff)+360)%360
elif Cmax == G:
    h = (60*((B-R)/diff)+120)%360
elif Cmax == B:
    h = (60*((R-B)/diff)+240)%360

if Cmax == 0:
    s = 0
else:
    s = (diff/Cmax)*100

v = Cmax*100

print("Wartości w HSV: ","H =" ,h, "S =" ,s, "V =",v)