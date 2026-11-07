n = 172
base = 16
s = ""
while n > 0:
    a = n % base
    s = str(a) + s
    n = n // base
print(s)