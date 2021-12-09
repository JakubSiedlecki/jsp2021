n = int(input("Podaj liczbę wyrazów szeregu harmonicznego: "))

x = 1                      # pierweszy wyraz i jednocześnie licznik pozostałych wyrazów
y = 0

for i in range(n-1):       # (n - 1) bo pierwszy wyraz x jest dodawany odzielnie na końcu
    z = x/(i+2)            # z to wyrazów, które są ułamkami, dzielę przez (i+2) ponieważ dla samego i nie można podzielić przez zero, a (i+1) dla i równego 0 spowodowałoby powstanie wyrazu identycznego do pierwszego 
    y +=z                  #  zmienna y powiększa się przy każdym przejściu petli o wartość następnego wyrazu (ułamka)

print("Suma n pierwszych wyrazów szeregu harmonicznego wynosi: ",x+y)       # (x+y), żeby zsumować wyraz pierwszy oraz sumę pozostałych wyrazów (ułamków)