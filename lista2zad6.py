list=["Kasia","Basia","Marek","Darek"]
print(list)
list.append("Józek",)                        #polecenie 'append' dodaje dany element na końcu listy
print(list)
list.extend(["Ania","Basia"])                #polecenie 'extend' dodaje elementy (które trzbea podać jako jedną listę) na końcu listy, którą chcemy powiększyć
print(list)
list.sort()                                  #polecenie 'sort' ustawia elementy listy w koljeności alfabetycznej
print(list)
print(list[3])                               #'print(list[3])' ponieważ chcemy zobaczyć czwarty element, a pierwszy jest oznaczony jako [0]
print(list[0:2])                             
print(list[-2:])
list.remove("Basia")                         #na pewno jest jakiś lepszy spób, ale nie miałem pomysłu
list.remove("Basia")
print(list)
print(len(list))                             #'len(list)' zwraca ilość elementów listy
krotka=tuple(list)                           #najpierw należy zdefiniować nazwę krotki, a dopiero potem użyć polecenia tuple(nazwa listy zamienianej na krotkę)   
print(krotka)
