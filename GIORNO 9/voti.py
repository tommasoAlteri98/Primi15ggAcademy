studenti = []

media = []

condizione = True
while condizione:
   print("-------------| Menu |-------------")
   print("1. Aggiungi studente e voto ")
   print("2. Mostra Studenti ")
   print("3. Stop")


   scelta = int(input("Seleziona un'opzione: "))

   if scelta == 1:
      nome = input("Inserisci nome alunno ")
      quantità_voti = int(input("Inserisci quanti voti vuoi: "))
      for pippo in range(quantità_voti):
        voto = int(input("Inserisci voto "))
        media.append(voto)
      voto_media = sum(media) / len(media)
      studenti.append({"Nome" : nome, "Media" : voto_media})
   elif scelta == 2:
      for i in studenti:
       print( "Nome: ", i["Nome"], ", Media:", i["Media"])
   elif scelta==3:
      condizione = False
      print("Programma terminato.")
   else:
      print("Opzione non valida! Riprova.")