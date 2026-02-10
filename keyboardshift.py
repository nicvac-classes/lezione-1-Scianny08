#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
sys.stdin = open('keyboardshift_input0.txt')
sys.stdout = open('output.txt', 'w')

# input data
N = int(input().strip())
S = input().strip()

# insert your code here
righe = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
tastiera = {}

for riga in righe:                      #per ogni riga
    for i in range(len(riga)-1):        #da indice 0 fino alla lunghezza della riga - 1
        tastiera[riga[i]] = riga[i+1]   #assegna a key lettera corrente il value della lettera a destra
    tastiera[riga[-1]] = riga[0]        #all'ultima mette la prima lettera della riga

# Trasformiamo S in lista per poter modificare i caratteri
S = list(S)

for i in range(len(S)):
    char_corrente = S[i]
    if char_corrente in tastiera:
        S[i] = tastiera[char_corrente]

# Ricostruzione della stringa sovrascrivendo S senza usare join
temp = ""
for char in S:
    temp += char
S = temp

# Scrittura del risultato nel file output.txt
print(S)