

#Apertura del file.txt
with open("file.txt", "r") as f:
    r = f.read()

    p = r.split()

    print("conta parole: ",len(p))

#quante righe ci sono nel file
#print(f"numero righe: {len(r)}")

