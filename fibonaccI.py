# fibonacci by using generators
def gen(n):
    a = -1
    b = 1
    while n != 0:
        c = a + b
        yield c
        a = b
        b = c
        n -= 1


g = gen(50)
for i in g:
    print(i)


# ?______________or---------------
def fec(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
h=fec(50)
for j in h:
    print(j)