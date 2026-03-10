# https://training.olinfo.it/task/turni

import sys

# Per la sottoposizione di questo problema in piattaforma: ATTIVARE QUESTE DUE RIGHE!
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

K = int(input())
N = int(input())

persone = []
for _ in range(N):
    a, b = map(int, input().split())
    persone.append((a, b))

risposta = 0

# SCRIVI QUI LA SOLUZIONE
persone.sort()

risposta = 0
coperto_fino_a = -1
i = 0

while coperto_fino_a < K - 1:
    miglior_fine = -1
    
    while i < N and persone[i][0] <= coperto_fino_a + 1:
        if persone[i][1] > miglior_fine:
            miglior_fine = persone[i][1]
        i += 1
    
    coperto_fino_a = miglior_fine
    risposta += 1

print(risposta)