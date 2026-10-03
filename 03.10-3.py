print("введите натуральное число")
n = int(input())
for i in range(1, n + 1):
    b = bin(i)[2:]
    h = hex(i)[2:]
    print(i, b, h)
