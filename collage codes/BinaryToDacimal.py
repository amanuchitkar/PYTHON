binary="100011"
if set(binary)<={"1","0"}:
    decimalOut=0
    power=len(binary)-1
    for bit in binary:
        decimalOut+=int(bit)*(2**power)
        power-=1
    print(decimalOut)

# binary_input = input("Enter a binary number: ")

# # Check if the input is a valid binary number
# if all(bit == '0' or bit == '1' for bit in binary_input):
#     decimal_output = 0
#     power = len(binary_input) - 1
    
#     for bit in binary_input:
#         decimal_output += (int(bit) << power)
#         power -= 1
    
#     print("Decimal equivalent:", decimal_output)
# else:
#     print("Invalid binary number entered.")
