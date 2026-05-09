while True:
    print("1. Calcolatrice")
    print("2. Pari o dispari")
    print("3. Classifica età")
    print("4. Esci")
    scelta = int(input("Scegli un'opzione: "))

    if scelta == 1:
        operazione = input("che operazione vuoi eseguire? :")
        if operazione not in ["+", "-", "*", "/"]:
            print("errore")
            continue
        numero1 = float(input("inserisci il primo numero: "))
        numero2 = float(input("inserisci il secondo numero: "))
        if operazione == "+":
            risultato = numero1 + numero2
        elif operazione == "-":
            risultato = numero1 - numero2
        elif operazione == "*":
            risultato = numero1 * numero2
        elif operazione == "/":
            if numero2 == 0:
                risultato = "impossibile dividere per 0"
            else:
                risultato = numero1 / numero2
        print(numero1, operazione, numero2, "=", risultato)
    elif scelta == 2:
        numero=int(input("inserisci un numero:" ))
        if numero%2==0:
            print("il numero è pari")
        else:
            print("il numero è dispari")
    
    elif scelta == 3:
        eta=int(input("Inserisci la tua età: "))

        if eta<13:
            print("Sei un bambino")
        elif eta<18:
            print("Sei un adolescente")
        elif eta<65:
            print("Sei un adulto")
        else:
             print("Sei un anziano")
    

    elif scelta == 4:
        print("Arrivederci!")
        break
    else:
        print("errore, opzione non valida")

