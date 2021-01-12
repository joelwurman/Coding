number_of_months = 35
new_rabbits_per_rabbit = 3
rabbits_now = 1
rabbits_last_month = 0
rabbits_this_month = rabbits_now
print(rabbits_now)

for months in range(number_of_months - 1):
    rabbits_this_month = rabbits_now
    rabbits_now = rabbits_this_month + rabbits_last_month * new_rabbits_per_rabbit
    rabbits_last_month = rabbits_this_month
    print(rabbits_now)


def fibo(n):
    if n == 0 or n == 2 :
        return 1
    else :
        return fibo(n) + fibo(n-1)