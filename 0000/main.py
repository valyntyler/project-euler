def odd(n: int) -> bool:
    return n % 2 != 0


sum = 0
top = 446e3

for i in range(1, int(top) + 1):
    print(i**2)
    if odd(i):
        sum += i**2

print(sum)
