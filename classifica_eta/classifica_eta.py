#Input: età Output: <13 → bambino <18 → adolescente <65 → adulto altrimenti → anziano

eta=int(input("Inserisci la tua età: "))

if eta<13:
    print("Sei un bambino")
elif eta<18:
    print("Sei un adolescente")
elif eta<65:
    print("Sei un adulto")
else:
    print("Sei un anziano")