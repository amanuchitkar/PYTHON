# # lis = ["1", "8", "67", "90"]
#
# # for i in range(len(lis)):
# #     lis[i] = int(lis[i])
# # ---------------OR-------------
# # lis = list(map(int, lis))
# # lis[2] = lis[2] + 9
# # print(lis[2])

# # n = [5, 6, 7, 3, 2]
# # def sq(a):
# #     return a * a
# # square = list(map(sq, n))
# # print(square)


# n = [5, 6, 7, 3, 2]
# square = list(map(lambda a: a * a, n))
# print(square)

# def square(a):
#     return a * a
#
#
# def cube(a):
#     return a * a * a
#
#
# func = [square, cube]
# i = 0
# while i < 5:
#     var = list(map(lambda x: x(i), func))
#     print(var)
#     i += 1


# lis1 = [111, 2, 4, 6, 8, 3, 9, 8, 10]
#
#
# def graterThan_5(a):
#     return a > 5
#
#
# lis_g_5 = list(filter(graterThan_5, lis1))
# print(sorted(lis_g_5))
from functools import reduce

num = [1, 2, 3, 4, 5, 6]
# x=0
# for i in num:
#     x=x+i
m = reduce(lambda x, y: x + y, num)
n = reduce(lambda x, y: x * y, num)
# q = reduce(lambda x, y: x % y, num)

print(m)
print(n)
# print(q)
