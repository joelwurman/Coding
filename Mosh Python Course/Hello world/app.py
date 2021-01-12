y = 0
for x in range(1, 10):
    print(x) if x % 2 == 0 else False
    y += 1 if x % 2 == 0 else False

print(f'total pair numbers is {y}')
