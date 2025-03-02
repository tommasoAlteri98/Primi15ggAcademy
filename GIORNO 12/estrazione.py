from random import randint

random_salvati = []

for n in range(5) :
    numeri_random = randint(1,20)
    random_salvati.append(numeri_random)

stringa_numeri = ",".join(str(n) for n in random_salvati)
punteggio = 0
tentativi = 0

with open ("salvanum.csv","w") as miofile :
    miofile.write(stringa_numeri)

with open ("salvanum.csv","r") as miofile :
    contenuto = miofile.read()
    
contenuto = contenuto.split(",")

for n in range(n) :
    try :
        numero_utente=input("inserisci un numero tra 1 e 20:")
        if numero_utente in contenuto :
            print("Hai indovinato uno dei numeri")
            punteggio +=1
            tentativi += 1
            print("Punteggio attuale:"+str(punteggio))
            print("Numero tentativi:"+str(tentativi))
        else :
            print("Il numero non è corretto")
            tentativi += 1
            print("Punteggio attuale:"+str(punteggio))
            print("Numero tentativi:"+str(tentativi))

        if punteggio == 2 :
            print("Hai vinto!")
            break
        elif tentativi == 5 and punteggio < 2 :
            print("Hai perso!")
        
    except :
        print("inserisci un valore corretto ")