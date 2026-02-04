#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
<<<<<<< HEAD
sys.stdin = open('spegnitutto_input_1.txt')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())

=======
sys.stdin = open('spegnitutto_input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())
>>>>>>> 4d04c5f2de5055f14f1d081173806103ba6d8aa0
for test in range(1, T+1):
    input()
    N = int(input().strip())

    A = list(map(int, input().strip().split()))

    ris = 0
<<<<<<< HEAD


    # INSERISCI IL TUO CODICE QUI
    i = 0
=======
    i = 0

    # INSERISCI IL TUO CODICE QUI
>>>>>>> 4d04c5f2de5055f14f1d081173806103ba6d8aa0
    while i < N:
        if A[i] == 1:
            consecutivi = 0
            while i<N and A[i] == 1:
                consecutivi += 1
                i += 1
<<<<<<< HEAD
            ris += (consecutivi + 1)//2
        else:
            i += 1
            
    print("Case #%d: " % test, end='')
    print(ris)

=======
            ris += (consecutivi +1)//2
        else:
            i += 1
    

    print("Case #%d: " % test, end='')
    print(ris)
>>>>>>> 4d04c5f2de5055f14f1d081173806103ba6d8aa0
sys.stdout.close()
