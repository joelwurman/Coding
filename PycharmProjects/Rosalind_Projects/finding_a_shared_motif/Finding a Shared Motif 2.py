from Bio import SeqIO
import sys
from Progress_bar import update_progress
import numpy as np

sequences = np.array([str(seq.seq) for seq in SeqIO.parse("rosalind_lcsm.txt", "fasta")])
# print(sequences)

###working from  below ##replace sequences[0] by seq1

# print('lalal', sequences)
# seq1 = 'GATTACA'
# # seq1 = 'GATT'
# seq2 = 'TAGACCA'
# seq3 = 'ATACA'
# sequences = [seq1, seq2, seq3]


##########################################################
# create unique subsequences from first sequence
subsequences = []
counter = 0
print(sequences[0], len(sequences[0]))
for x in range(len(sequences[0])):
    for y in range(x):
        if sequences[0][y:x] not in subsequences:
            subsequences.append(sequences[0][y:x])
    if sequences[0][x:] not in subsequences:
        subsequences.append(sequences[0][x:])
    counter += 1/len(sequences[0])
    update_progress(counter / 101)

print('1 Subsequences of first sequence: ', subsequences)
possible_subsequences = subsequences

# # check if subsequences in sequences
# for current_seq in sequences:
#     for current_subseq in subsequences:
#         print('2 analysing: ', current_subseq, ' in ', current_seq)
#         if current_subseq not in current_seq:
#             possible_subsequences.remove(current_subseq)
#             print('3 ', current_subseq, ' NOT IN ', current_seq)
#         elif current_subseq in current_seq:
#             print('4 ', current_subseq, ' Yes IN ', current_seq)
#         print('5 Subsequences left: ', possible_subsequences, '\n')

# check if subsequences in sequences, second attempt
x = []
max_subsequence = ''
for current_subseq in subsequences:
    score = 0
    for current_seq in sequences:
        if current_subseq in current_seq:
            score += 1
    if score == len(sequences):
        x.append(current_subseq)
        if max_subsequence < current_subseq:
            max_subsequence = current_subseq
print(x, 'max subseq: ', max_subsequence)
# print(max(possible_sequences))
