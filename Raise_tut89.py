# a = input("Enter your name: ")
# b = int(input("How much you earn: "))
# if b == 0:
#     raise ZeroDivisionError("b is 0 stop the program")
# if a.isnumeric():
#     raise Exception("Number nhi chiye naam likh>>")
# print(f"hello {a}")



c=input("enter your name: ")
try:
    print(a)
except Exception as e:
    if c=="aman":
        raise ValueError("aman is blocked ")
    print("Exception Handled")