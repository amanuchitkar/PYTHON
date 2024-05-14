# try:
#     # Input the lengths of the three sides of the triangle
#     a = float(input("Enter the length of the first side: "))
#     b = float(input("Enter the length of the second side: "))
#     c = float(input("Enter the length of the third side: "))

#     # Ensure the sides are positive numbers
#     if a <= 0 or b <= 0 or c <= 0:
#         print("All sides must be positive numbers.")
#     else:
#         # Check if the triangle is right-angled
#         if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
#             print("The triangle is a right-angled triangle.")
#         else:
#             print("The triangle is not a right-angled triangle.")
# except ValueError:
#     print("Invalid input. Please enter numeric values for the sides.")

# a = [3]
# b = a
# c = 3
# print(a is b)  # True, because a and b reference the same object
# print(a is c)  # False, because a and c reference different objects with the same content
