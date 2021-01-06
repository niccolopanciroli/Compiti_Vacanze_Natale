print("Crea un programma che scriva la differenza di due numeri a e b se il loro prodotto è maggiore di 10, oppure la loro somma se il prodotto è minore o uguale a 10.")
print()
a = int(input("Inserisci il primo numero"))
b = int(input("Inserisci il secondo numero"))

if a*b>10:
    print("La differenza tra a e b è: ", a-b)
else:
    print("La somma tra a e b è: ", a+b)