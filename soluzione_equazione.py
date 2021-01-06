a= int(input("Inserisci il primo numero "))
b= int(input("Inserisci il secondo numero "))

if a==0 and b==0:
    print("L'equazione è indeterminata")
elif a== 0 and b!=0:
    print("L'equazione è impossibile")
elif a!=0 and b==0:
    print("La soluzione dell'equazione è X=0")
elif a!=0 and b!=0:
    soluzione= -(b/a)
    print("La soluzione dell'equazione è ", soluzione)