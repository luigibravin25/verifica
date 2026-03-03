#Apertura del file.txt
with open("file.txt", "r") as f:
    r = f.readlines()
    

#quante righe ci sono nel file
print(f"numero righe: {len(r)}")
