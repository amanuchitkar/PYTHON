import time
from functools import lru_cache

print("func is calling")
x = int(input(":"))


@lru_cache(maxsize=x)
def func(n):
    time.sleep(n)
    return n


print("func is calling")
func(3)
# func(2)
print("Done calling func")
func(3)
print("calling func again")
func(3)
print("calling func again")
