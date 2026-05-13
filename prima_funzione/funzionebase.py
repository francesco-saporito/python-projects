
#esempio funzione senza input

def saluta():
    print('Ciao, benvenuto!')

saluta()    

def somma(a, b):
    return a + b

def saluta_nome(nome):
    print('ciao, ' + nome + '!')

print('come ti chiami?')
nome = input()
saluta_nome(nome)    

print('inserisci il primo numero: ')
a = float(input())
print('inserisci il secondo numero: ')
b = float(input())

print('la somma è: ' + str(somma(a, b)))

print('vuoi farne un altra? (s/n)')

risposta = input()


while risposta == 's':
    print('inserisci il primo numero: ')
    a = float(input())
    print('inserisci il secondo numero: ')
    b = float(input())

    print('la somma è: ' + str(somma(a, b)))

    print('vuoi farne un altra? (s/n)')
    risposta = input()

print("A presto ", nome + "!")