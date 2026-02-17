#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

# input data
N = int(input().strip())

ris = 0
for i in range(N):
    S = input().strip()

    # insert your code here
    diz = {}
    
    pulita = ""
    for chr in S:
        if chr.isalpha():
            pulita += chr
    
    pulita = pulita.lower()
    
    for chr in pulita:
        if chr in diz:
            diz[chr] += 1
        else:
            diz[chr] = 1
    
    valido = True
    for valore in diz.values():
        if valore > 2:
            valido = False
            break
    
    if valido:
        ris += 1
            
print(ris)  # print the result
