from Bio import SeqIO
import sys
from Progress_bar import update_progress
import numpy as np

sequences = list(np.array([str(seq.seq) for seq in SeqIO.parse("rosalind_lcsm.txt", "fasta")]))
print(sequences)


shared_subsequences = []

for x in range(len(sequences[0])):
    print('x is ', x)
    for y in range(x+1):
        fragment = sequences[0][y:x+1] ## this line generates the current fragment to test
        print("fragment is ", fragment)

        for sequence in sequences:
            print(fragment, " in ", sequence)
            if fragment not in sequence:
                print("absent, breaking")
                break
            elif (sequence == sequences[-1]) and (fragment not in shared_subsequences):
                print("present, adding", fragment)
                shared_subsequences += str(fragment)
            else:
                print('present but not adding')
            # print(shared_subsequences)
    print('shared sequences: ', shared_subsequences)
