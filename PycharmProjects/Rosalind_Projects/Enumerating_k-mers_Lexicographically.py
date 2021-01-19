# from itertools import permutations
# from itertools import combinations_with_replacement

symbols = "A G C T"
length = 2

char_list = sorted(symbols.split(' '))
a, b = [], []
for n in range(length):
    a.append(char_list[0])
    b.append(char_list[-1])
print(b)

final_list = []

while a != b:
    i = -1
    a[]

# char_list = sorted(symbols.split(' '))
# print(char_list)
# # Get all permutations of length 2
# # and length 2
# perm = permutations(char_list, length)
# perm += cm(char_list, length)
# for x in list(perm):
#     print(''.join(x))
