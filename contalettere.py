parola = str(input("Inserisci una parola: ")).lower().strip()

diz = {}
i = 97
while i <= 122:
    diz[chr(i)] = 0
    i += 1
    
for char in parola:
    if char in diz:
        diz[char] += 1

print(diz)