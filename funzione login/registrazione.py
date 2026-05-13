

utentetest = ""
passwordtest = ""

def menu():
    print("1. Login")
    print("2. Registrazione")
    print("3. Esci")

def registrazione():
    global utentetest, passwordtest
    print("Inserisci il tuo nome utente:")
    utentetest = input()
    print("Inserisci la tua password:")
    passwordtest = input()
    print("Registrazione avvenuta con successo!")

def login():

    print("Inserisci il tuo nome utente:")
    username = input()
    print("Inserisci la tua password:")
    password = input()

    if username == utentetest and password == passwordtest:
        print("Accesso consentito!")
        exit()

    else:
        print("Nome utente o password errati!")

def esci():
    print("Arrivederci!")
    exit()


while True:
    menu()
    scelta = int(input("Scegli un'opzione: "))
    if scelta == 1:
        login()
    elif scelta == 2:
        registrazione()
    elif scelta == 3:
        esci()
        break
    else:
        print("Errore, opzione non valida")