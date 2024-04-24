decimal_num = 93
binary_num = 0
position = 1

if decimal_num == 0:
    binary_num = 0
else:
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num += remainder * position
        position *= 10
        decimal_num //= 2

print("Binary representation:", binary_num)