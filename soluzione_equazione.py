a= int(input("Inserisci il primo coefficiente della x"))
b= int(input("Inserisci il termine noto"))

if a==0 and b==0:
    print("L'equazione è indeterminata")
elif a== 0 and b!=0:
    print("L'equazione è impossibile")
elif a!=0 and b==0:
    print("La soluzione dell'equazione è X=0")
elif a!=0 and b!=0:
    soluzione= -(b/a)
    print("La soluzione dell'equazione è ", soluzione)