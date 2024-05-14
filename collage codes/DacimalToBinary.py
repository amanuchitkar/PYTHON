dacimal_num=35
old_dacimal_num=dacimal_num
binary_num=""
if dacimal_num==0:
        print("0")
while dacimal_num>0:
        remainder=dacimal_num%2
        binary_num=str(remainder)+binary_num
        dacimal_num//=2
print(f"The Dacimal Number {old_dacimal_num} in Binary is {binary_num}")

# position=1
# if dacimal_num==0:
#         print("0")
# while dacimal_num>0:
#         r=dacimal_num%2
#         binary_num+=r*position
#         position*=10
#         dacimal_num//=2
# print(f"The Dacimal Number {old_dacimal_num} in Binary is {binary_num}")
        