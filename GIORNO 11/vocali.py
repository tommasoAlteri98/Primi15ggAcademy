fraseInput = input("Inserisci una frase: ")
vocali = "AEIOUaeiou"
listaPush = []

for i, lettera in enumerate(fraseInput):
    if lettera in vocali:
        listaPush.append((lettera, i))

for vocale, indice in listaPush:
    print("Vocale: " + vocale + " - Indice: " + indice)