from Bio import SeqIO

#####################################################

# parsing a fasta file

for sequence in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(sequence.id)
    print(sequence.seq)
    print(len(sequence))
    print(repr(sequence.seq))
print(SeqIO.parse("ls_orchid.fasta", "fasta")[0])

#####################################################

# # sequences act like stings
#
# for index, letter in enumerate(my_seq):
#     print("%i %s" % (index, letter))