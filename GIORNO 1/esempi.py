print("Benvenuto nel minigioco a 3 livelli")
domanda1 = input("Prima domanda: Qual è la capitale d'Italia?")
if domanda1 == "Roma" : domanda2 = input("Esatto! Seconda domanda: Qual è la capitale della Francia?")
else : print("Hai sbagliato, peccato.")
if domanda2 == "Parigi" : domanda3 = input("Esatto! Terza domanda: Qual è la capitale della Germania?")
else : print("Hai sbagliato, peccato.")
if domanda3 == "Berlino" : print("3 su 3! Bravissimo, hai vinto!!")
else : print("Hai sbagliato, peccato.")