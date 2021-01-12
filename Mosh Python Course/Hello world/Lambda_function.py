items = [
    ('product 1', 46),
    ('product 2', 12),
    ('product 3', 34),
    ('product 4', 9),
]

# items.sort(key=lambda item: item[1])
# print(items)

# filtered = list(filter(lambda item: item[1] >= 14, items))
# print(filtered)

# comprehension: [expression for item in items]
prices = [item for item in items if item[1] >= 14]
print(prices)
