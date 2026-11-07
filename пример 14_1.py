n = 7 * 49 ** 120 - 6 * 343 ** 65 - 5 * 7 ** 40
base = 7
count = 0
while n > 0:
    a = n % base
    if a == 6:
        count = count + 1
    n = n // base
print(count)

