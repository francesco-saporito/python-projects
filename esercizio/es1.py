# Esercizio 1 ricreo la calcolatrice senza guardare

num1=float(input("Inserisci il primo numero: "))
num2=float(input("Inserisci il secondo numero: "))

operazione = input("Che operazione vuoi eseguire? +, -, *, /")
if operazione!="+" and operazione!="-" and operazione!="*" and operazione!="/":
    print("Operazione non valida")
else:
    if operazione=="+":
        print("Il risultato è: ", num1+num2)
    elif operazione=="-":
        print("Il risultato è: ", num1-num2)
    elif operazione=="*":
        print("Il risultato è: ", num1*num2)
    elif operazione=="/":
        if num2==0:
            print("Non puoi dividere per zero") 
            exit()

        else:
            print("Il risultato è: ", num1/num2)