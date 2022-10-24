# tut #76
f1 = open("aman.txt")
try:
    f = open("does.txt")
# except Exception as e:
#     print(e)
except IOError as e:
    print("IOError error aaya he bhai",e)
except EOFError as e:
    print("EOFError Error aaya he bhai",e)
else:
    print("This will run if only except is not running")
finally:
    # f.close()
    print("Run this any way...")
    f1.close()
print("Important stuff.....")
