with open('rosalind_revc.txt', 'r') as input_file:
    dna = input_file.read()

reverse_complement = ''
for nucl in dna:
    if nucl == 'T':
        reverse_complement = "A" + reverse_complement
    if nucl == 'A':
        reverse_complement = "T" + reverse_complement
    if nucl == 'C':
        reverse_complement = "G" + reverse_complement
    if nucl == 'G':
        reverse_complement = "C" + reverse_complement
print(reverse_complement)

