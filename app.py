#Apertura del file.txt
with open("file.txt", "r") as f:
    p = f.readlines()
    
#quante righe ci sono nel file
print(len(p))