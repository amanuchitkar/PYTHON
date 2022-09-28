# l = 20  # Global.
#
#
# def function1(n):
#     # l = 5  # Local.
#     m = 6  # Local.
#     global l  # give access to change Global l from any local locality.
#     l = l + 45
#     print(l, m, "I have printed")
#
#
# function1("hello")
# print(l)
# print(m)

def aman():
    y = 5

    def nayan():
        global y
        y = 55

    print("before calling nayan", y)
    nayan()
    print("After calling nayan", y)


aman()
print("y print globaly, global y make y as a global variable",y)
