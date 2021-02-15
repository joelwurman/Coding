import matplotlib.pyplot as plt


def is_prime(x):
    for n in range(2, x):
        if x % n == 0:
            return False
    else:
        return True


current_number, current_index = 1, 1
prime_numbers = [[1, 1]]

while current_index < 10:
    current_number += 1
    if is_prime(current_number):
        current_index += 1
        prime_numbers.append([current_index, current_number])
print(prime_numbers)
plt.scatter(prime_numbers[0], prime_numbers[1])
plt.show()
