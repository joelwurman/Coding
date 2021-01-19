from Bio import SeqIO

sequences = []
handle = open('../rosalind_lcsm.txt', 'r')
for record in SeqIO.parse(handle, 'fasta'):
    sequence = []
    seq = ''
    for nt in record.seq:
        seq += nt
    sequences.append(seq)
handle.close()
print(sequences)


srt_seq = sorted(sequences, key=len)
short_seq = srt_seq[0]
comp_seq = srt_seq[1:]
motif = ''
for i in range(len(short_seq)):
    for j in range(i, len(short_seq)):
        m = short_seq[i:j + 1]
        print('1 ', m)
        found = False
        for sequ in comp_seq:
            print('2 ', sequ)
            if m in sequ:
                found = True
            else:
                found = False
                break
        if found and len(m) > len(motif):
            motif = m
print(motif)
