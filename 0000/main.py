from math import sqrt


def odd(n: int) -> bool:
    return n % 2 != 0


def perfect_square(n: int) -> bool:
    return int(sqrt(n)) ** 2 == n


sum = 0
n = 1
i = 446e3

while i != 0:
    if perfect_square(n):
        sum += n * int(odd(n))
        i -= 1
        print(n)
    n += 1

print(sum)
