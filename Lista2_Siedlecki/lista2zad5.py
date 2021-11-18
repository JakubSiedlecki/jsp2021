napis=input("Podaj napis o parzystej liczbie znaków: ")                                                                                                           
połowa=len(napis)//2                                                                                      # 'len()' zwraca ilość znaków w napisie, "//2" potrzebuję znać połowę długości wyrazu bez reszty
część1=napis[0:połowa]+"[Python]"                                                                         # pierwsza połowa nowego wyrazu 
część2=napis[połowa:]                                                                                     # druga połowa nowego wyrazu     
print("Napis powstały po wstawieniu do środka pierwotnego napisu '[Python]': ",część1+część2)             # nowy wyraz  