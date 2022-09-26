# a = 4
# b = 5
# c = sum((a, b))
def function1():
    print("Your are in function 1")


# print(function1())
function1()


def function2(a, b):
    """This is a function which will calculate average of two number"""
    avrag = (a + b) / 2
    return avrag


print(function2.__doc__)
# v = function2(5, 7)
# print(v)
