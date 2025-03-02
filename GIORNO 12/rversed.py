fraseInput = input("Inserisci una frase: ").lower()
listaCar = []

def palindromo() :
    listaFrase = list(fraseInput)
    
    for x in listaFrase :
        if x.isalpha() :
            listaCar.append(x)
    listaReversed = list(reversed(listaCar))
    
    if listaReversed == listaCar :
        print("La frase inserita è palindroma")
    else :
        print("La frase inserita non è palindroma")

palindromo()