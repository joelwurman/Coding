def fibonacci(x):
    y = int
    if x > 1:
        return fibonacci(x - 1) + fibonacci(x - 2)
    else:
        return x



while True:
    print(fibonacci(int(input())))
    print('\n')
