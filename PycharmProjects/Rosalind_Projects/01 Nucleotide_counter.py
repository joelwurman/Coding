with open('rosalind_dna (1).txt', 'r') as input_file:
    dna = input_file.read()

a, t, c, g = 0, 0, 0, 0

for nucleotides in dna:
    if nucleotides == 'A':
        a += 1
    if nucleotides == 'T':
        t += 1
    if nucleotides == 'C':
        c += 1
    if nucleotides == 'G':
        g += 1

print(f'{a}=a {c}=c {g}=g {t}=t')

# second method
print(f'''{dna.count('A')}=A {dna.count('C')}=C {dna.count('G')}=G {dna.count('T')}=T''')
