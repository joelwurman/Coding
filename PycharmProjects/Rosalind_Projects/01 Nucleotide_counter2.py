with open('rosalind_dna (1).txt', 'r') as input_file:
    dna = input_file.read()

# second method
print(f'''{dna.count('A')} {dna.count('C')} {dna.count('G')} {dna.count('T')}''')
