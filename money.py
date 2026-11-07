s = int(input())
c10 = s // 10
s = s % 10
c5 = s // 5
s = s % 5
c2 = s // 2
s = s % 2
c1 = s
if c10 > 0:
    print(c10, "по 10 руб.")
if c5 > 0:
    print(c5, "по 5 руб.")
if c2 > 0:
    print(c2, "по 2 руб.")
if c1 > 0:
    print(c1, "по 1 руб.")
