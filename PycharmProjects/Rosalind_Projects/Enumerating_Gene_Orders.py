from itertools import permutations

n = int(6)

perm = permutations(range(1, n + 1), n)

output = ""
for x in perm:
    for i in x:
        output += str(i) + " "
    else:
        output += "\n"
print(output.count("\n"))
print(output)
