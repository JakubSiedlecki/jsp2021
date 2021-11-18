list=list(range(3,100,3))         #(3,100-zasięg/rozmiar listy | 3 na końcu oznacza przeskok argumentów listy)
print(list)
del list[4::3]                    #'del' usuwa wybrane elementy zaczynając od piątego, a następnie usuwa co trzeci element 
print(list)
suma=sum(list)                    #suma argumentów pozostałych w liście
arg=len(list)                     #ilość argumentów pozostałych w liście
print("średnia= ", suma/arg)
