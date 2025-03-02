fraseInput = input("Inserisci una stringa: ")
frequenzeLettere = {}

for l in fraseInput:
    if l in frequenzeLettere:
        frequenzeLettere[l] += 1  
    else:
        frequenzeLettere[l] = 1  
print(frequenzeLettere)