import numpy as np
from collections import Counter

with open('rosalind_cons.txt', 'r') as input_file:
    input_dna = input_file.read()

input_dna = input_dna.split('\n')

# make array
dna_array = []
sequence_number = 0
sub_array = []
for line in input_dna:
    if line[0] == '>':
        sequence_number += 1
        if sub_array:
            dna_array.append(sub_array)
            sub_array = []

    elif line[0] != '>':
        for char in range(len(line)):
            sub_array += line[char]
dna_array.append(sub_array)
Profile_array = np.zeros((4, len(dna_array[1]))).astype(int)

# count all of the first column
current_counts = ''
for paragraph in range(sequence_number):
    for character in range(len(dna_array[0])):
        current_counts += dna_array[paragraph][character]
    # print(paragraph, dict(Counter(current_counts)))
    Profile_array[0][paragraph] = Counter(current_counts)['A']
    Profile_array[1][paragraph] = Counter(current_counts)['C']
    Profile_array[2][paragraph] = Counter(current_counts)['G']
    Profile_array[3][paragraph] = Counter(current_counts)['T']

    current_counts = ''

# find concensus
consensus_sequence = ''
for consensus_nucleotide in range(len(Profile_array[0])):
    # print(np.amax(Profile_array, axis=0)[consensus_nucleotide], Profile_array[0][consensus_nucleotide])
    if np.amax(Profile_array, axis=0)[consensus_nucleotide] == Profile_array[0][consensus_nucleotide]:
        consensus_sequence += 'A'
    if np.amax(Profile_array, axis=0)[consensus_nucleotide] == Profile_array[1][consensus_nucleotide]:
        consensus_sequence += 'C'
    if np.amax(Profile_array, axis=0)[consensus_nucleotide] == Profile_array[2][consensus_nucleotide]:
        consensus_sequence += 'G'
    if np.amax(Profile_array, axis=0)[consensus_nucleotide] == Profile_array[3][consensus_nucleotide]:
        consensus_sequence += 'T'
print(consensus_sequence)

# print(str(Profile_array[0]).replace('[', 'A: ').replace(']', ''))
# print(str(Profile_array[1]).replace('[', 'C: ').replace(']', ''))
# print(str(Profile_array[2]).replace('[', 'G: ').replace(']', ''))
# print(str(Profile_array[3]).replace('[', 'T: ').replace(']', ''))
