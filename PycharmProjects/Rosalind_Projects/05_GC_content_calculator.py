with open('rosalind_gc.txt', 'r') as file:
    input_file = file.read()

formatted_file = input_file.replace('\n', '')
formatted_file = formatted_file.split('>')
formatted_file.pop(0)

for sequence in formatted_file:
    print(sequence[0: 13])
    a = ((sequence.count('C') + sequence.count('G')) * 100 / (
            sequence.count('A') + sequence.count('T') + sequence.count('G') + sequence.count('C')))
    print(a)
