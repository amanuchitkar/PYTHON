# def minus(a, b):
#     return a - b
#
#
# minus = lambda a, b: a - b
# print(minus(7,5))
# def a_first(a):
#     return a[0]
a = [[2, 51], [8, 14], [4, 34], [3, 15]]
a.sort(key=lambda x: x[1])  # lamda work as a_first function
print(a)
