# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
# def factorial_Iterative(n):
#     """

#     :param n:Integer
#     :return: n * n-1 * n-2 * n-3.......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac


# def factorial_Recursive(n):
#     """

#     :param n: Integer
#     :return: n * n-1 * n-2 * n-3........1
#     """
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial_Recursive(n - 1)


# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120

# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter a number: "))
# print("Factorial Using Iterative Method", factorial_Iterative(number))
# print("Factorial Using Recursive Method", factorial_Recursive(number))
print("Fibonacci num : ", fibonacci(number))
