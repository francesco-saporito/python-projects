#genera un login che fa entrare se nome utente e password sono corretti (admin e 1234)

admin="admin"
password="1234" 
nome_utente=input("Inserisci il nome utente: ")
password_utente=input("Inserisci la password: ")

if nome_utente==admin and password_utente==password:
    print("Accesso riuscito")
else:
    print("Accesso negato")
    exit()