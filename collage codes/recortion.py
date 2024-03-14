# # factorial function
# def facto(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*facto(n-1)
# a=9
# print(facto(a))

# def fibonachii(n):
#     if n<=1:
#         return 1
#     else:
#         return fibonachii(n-2)+fibonachii(n-1)

# for i in range(a):

#     print(fibonachii(i),end=" ")

def fib(n,a=1,b=1,count=0):
    if n<=1:
        print(1)
    elif count<n:
        print(a,end=" ")
        fib(n,b,a+b,count+1)

a=9
fib(9)