items = [
    ('product 1', 46),
    ('product 2', 12),
    ('product 3', 34),
    ('product 4', 9),
]


# prices = []
# for item in items:
#     prices.append(item[1])

x = map(lambda item: item[1], items)
for item in x:
    print(item)
