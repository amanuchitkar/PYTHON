name="Nayan"
# name=name.lower()
# name=name.replace(" ","")

# if name==name[::-1]:
#     print("yes")
# else:
#     print("no")

def palindrome(name):
    name=name.lower()
    name=name.replace(" ","")
    return name==name[::-1]
if palindrome(name):
    print("yes")
else:
    print("no")