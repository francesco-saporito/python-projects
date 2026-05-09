numero=0
password=""
while numero <= 5:
    print('ciclo del while :', numero)
    numero+=1

while password!="1234":
    password=input("Inserisci la password: ")
    if password!="1234":
        print("Password errata, riprova")
    else:
        print("Password corretta, accesso riuscito")


#GENERA UNA TABELINA CON for

for i in range(1,11):
    print('2*',i,'=',2*i)

# sommanumeri    con for 1+2+3...+n

print("Somma dei numeri da 1 a n")
n=int(input("Inserisci n: "))
somma=0
for i in range(1,n+1):
    print("i:", i, "somma: ", somma)
    somma=i+somma

# break e continue

for i in range(1,11):
    if i==8:
        break
    print(i)

for j in range(1,11):
    if j==5:
        continue
    print(j)