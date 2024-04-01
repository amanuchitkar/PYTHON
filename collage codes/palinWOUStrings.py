

num=int(input("enter input: "))
n=num
rev=0

while num!=0:
    d=num%10
    rev=(rev*10)+d
    num//=10

if n == rev:
    print("true")
else:
    print("error")

