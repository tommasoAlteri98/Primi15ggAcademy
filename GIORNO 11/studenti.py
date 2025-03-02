def calcolo_media_voti(voti,nome):
    if nome in voti:
        return sum(voti[nome])/len(voti[nome])
    else:
        return None

voti_studenti = {}

while True:
    print("Menu")
    print("1. Aggiungi studente")
    print("2. Media voti ")
    print("3. Esci")

    scelta = input("Seleziona un numero corrispettivo all'opzione:")

    if scelta == "1":

        nome_studente = input("Inserire nome dello studente da aggiungere:")
        voti = input("inserire i voti dello studente separati da spazio").split()
        voti_studenti[nome_studente] = [int(voto) for voto in voti]
        print("I voti di:",nome_studente)
    elif scelta == "2":
    
        studente= input("inserire il nome dello studente:")
    
        media = calcolo_media_voti(voti_studenti,studente)
        
        if media is not None:
            print("Media di " + studente + ": " + str(media))

        elif scelta == "3":
            print("chiusura script.")
            break
        else:
            print("scelta non valida.")
            

'''
Trasformate il programma che abbiamo creato in
precedenza per la gestione dei voti degli alunni in un
programma per la gestione di una classe che utilizza un
file come database:
All’avvio il programma chiede se si vuole leggere l’elenco
degli alunni e i loro voti e medie, se si vuole aggiungere un
alunno o un voto, se si vuole eliminare un alunno o un
voto.

'''