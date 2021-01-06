print("Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 0 è uguale a 2")
print()
numero= int(input("Inserisci un numero da verificare"))
if numero%2 == 0:
    print("Il numero ",numero, " è pari")
else:
    print("Il numero ",numero," è dispari")