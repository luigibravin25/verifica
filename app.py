

#Apertura del file.txt
with open("file.txt", "r") as f:
    r = f.read()


    l = r.splitlines()
    print("numero delle linee: ", len(l)) 
