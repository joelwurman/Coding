numbers = [1, 3, 5, 2, 5, 7, 4, 3, 2, 4, 5, 6, 0]
numbers2 = numbers.copy()

for item in numbers2:
    if numbers.count(item) > 1:
        numbers.remove(item)
    print(item)
    print(numbers)


