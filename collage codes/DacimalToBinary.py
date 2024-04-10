def dacimal_to_binary(decimal_num):
    binary_num=""
    if decimal_num==0:
        return "0"
    while decimal_num>0:
        reminder=decimal_num%2
        binary_num=str(reminder)+binary_num
        decimal_num//=2
    return binary_num

dacimal_num=35
binary_num=dacimal_to_binary(dacimal_num)
print(f"The Dacimal Number {dacimal_num} in Binary is {binary_num}")