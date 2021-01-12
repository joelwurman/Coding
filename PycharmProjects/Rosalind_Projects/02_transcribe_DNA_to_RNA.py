with open('rosalind_rna (1).txt', 'r') as input_file:
    dna = input_file.read()
rna = ''
for nucl in dna:
    if nucl == 'T':
        rna += 'U'
    else:
        rna += nucl
print(rna)
