def Somma():
    n_1 = int(input("Inserisci il primo numero: "))
    n_2 = int(input("Inserisci il secondo numero: "))
    risultato = n_1 + n_2
    print(f"{n_1} + {n_2} = {risultato}")

def Sottrazione():
    n_1 = int(input("Inserisci il primo numero: "))
    n_2 = int(input("Inserisci il secondo numero: "))
    risultato = n_1 - n_2
    print(f"{n_1} - {n_2} = {risultato}")

while True:
    print("Benvenuto nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta = int(input("1)sottrazione\n2)addizione\n0)exit\n"))
    if scelta == 0:
        break
    elif scelta == 1:
        Sottrazione()
    elif scelta == 2:
        Somma()
    else:
        print("Scelta non corretta!")
