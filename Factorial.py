# Generator for the factorial
def fac(num):
    facto = 1
    for i in range(1, num + 1):
        facto *= i
    yield facto


# Generator to generate the fibonacci series
def fib(number):
    f = 0
    s = 1
    for i in range(number):
        yield f
        f, s = s, f + s  # HERE: f = s(1)=1 and s= f(1)+s(1) = 2


fec = fac(4)
for i in fec:
    print(i)
