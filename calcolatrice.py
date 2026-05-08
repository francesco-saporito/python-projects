



operazione= input("che operazione vuoi eseguire? :")


if operazione not in ["+","-","*","/"] :
    print("errore")
    exit()

numero1= float(input("inserisci il primo numero: "))
numero2= float(input("inserisci il secondo numero: "))

if operazione == "+":
    risultato = numero1 + numero2

elif operazione == "-":
    risultato= numero1-numero2

elif operazione == "*":
    risultato= numero1*numero2

elif operazione == "/":
    if numero2 == 0:
        risultato = "impossibile dividere per 0"
    else:
        risultato = numero1/numero2

print(numero1, operazione, numero2, "=", risultato)