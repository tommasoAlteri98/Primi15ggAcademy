alfabeto = "abcdefghilmnopqrstuvz"
lista_alfabeto = list(alfabeto)
def cifrario():

    parola = input("Scrivi una parola: ")
    lista_parola = list(parola)
    chiave = int(input("Scegli una chiave per cifrare compresa tra 0 e 21: "))

    nuovo_alfabeto = lista_alfabeto[chiave:] + lista_alfabeto[:chiave]

    parola_cifrata = []

    for lettera in lista_parola:
        if lettera in lista_alfabeto:
            indice = lista_alfabeto.index(lettera)
            parola_cifrata.extend(nuovo_alfabeto[indice])
        else:
            parola_cifrata.extend(lettera)
    parola_cifrata = "".join(parola_cifrata)
    print("Parola cifrata:", parola_cifrata)

cifrario()

def de_cifrario():

    parola = input("Scrivi una parola: ")
    lista_parola = list(parola)
    chiave = int(input("Scegli una chiave per cifrare compresa tra 0 e 21: "))

    nuovo_alfabeto = lista_alfabeto[-chiave:] + lista_alfabeto[:-chiave]
    parola_cifrata = []

    for lettera in lista_parola:
        if lettera in lista_alfabeto:
            indice = lista_alfabeto.index(lettera)
            parola_cifrata.append(nuovo_alfabeto[indice])
        else:
            parola_cifrata.append(lettera)
    parola_cifrata = "".join(parola_cifrata)
    print("Parola cifrata:", parola_cifrata)

de_cifrario()