"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""


# generator_

def gen(n):
    for i in range(n):
        yield i


get = gen(6)
# print(get.__next__())
# print(get.__next__())
# print(get.__next__())
# print(get.__next__())
# --------OR__________
for i in get:
    print(i)

# Iterator
a = "mrudul"
itr = iter(a)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

# for c in a:
#     print(c)
