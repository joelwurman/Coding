from Bio.Seq import Seq

seq1 = 'GATTACA'
seq2 = 'TAGACCA'
seq3 = 'ATACA'
sequences = [seq1, seq2, seq3]

# create subsequences from first sequence
possible_sequences = []
counter = 1
for x in range(len(seq1)):
    for y in range(x):
        possible_sequences.append(seq1[y:x])
    possible_sequences.append(seq1[x:])


print(possible_sequences)

# check if subsequences in sequences
for current_seq in range(len(sequences)):
    for current_subseq in possible_sequences:
        print(sequences[current_seq], current_subseq)
        if current_subseq not in sequences[current_seq]:
            possible_sequences.pop(current_subseq.index(current_subseq))
        elif current_subseq in sequences[current_seq]:
            print('Repeated')
print('possible_sequences: ', possible_sequences)

print(max(possible_sequences))
