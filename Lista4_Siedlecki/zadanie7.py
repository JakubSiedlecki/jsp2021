def write_list(list):
    print(" ".join([str(item) for item in list]).center(50))

n = int(input("Podaj liczbę wierszy: "))
line = [1]            #pierwsza linia/wierzchołek trójkąta Pascala

#funkcja wpisująca pozostałe wiersze trójkąta pascala

write_list(line)
for i in range(n-1):    
    next_line = [1]                                 #wartość pierwszego elementu w nowej lini, krawędź tójkąta
    for j in range(len(line)-1):                    #wartość w środku trójkąta (len(line -1) bo po drugiej stronie trójkąta ma być 1
        next_line.append(line[j]+line[j+1])
    next_line.append(1)
    line = next_line
    write_list(line)


