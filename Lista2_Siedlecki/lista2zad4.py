napis=input("Podaj napis: ")
z1=napis[0]                         #pierwszy znak
reszta=napis[1:]                    #reszta znaków w podanym napisie
print(z1+napis.replace(z1, "@"))    #w tym przypadku print zwraca niezmieniony pierwszy znak z podanego napisu oraz zastępuje ten sam znak na '@', jeśli występuje on dalej w napisie
