f1 = open("logharry.txt", "a")
f2 = open("harryEx.txt", "a")


def getdate():
    import datetime

    return datetime.datetime.now()


t = getdate()


def harryfood(var):
    if var == "1":
        inp = input("What Harry Eat:")
        f = open("logharry.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("logharry.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("You choose something wrong, Please choose correct order ")


def harryexer(var):
    if var == "1":
        inp = input("What Harry done:")
        f = open("harryEx.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var == "2":
        f1 = open("harryEx.txt", "rt")
        r = f1.read()
        print(r)
        f1.close()
    else:
        print("You choose something wrong, Please choose correct order ")


print("Choose Persone: ")
print("1. Harry")
# per = input(":")
print("For what ?\n")
print("1. Food\n2. Exercise")
imp = input()
print("What do you want ?")
print("1. Log\n2. Retrive")
var = input()

if imp == "1":
    if var == "1" or var == "2":
        harryfood(var)
    else:
        print("You choose something wrong, Please choose correct order ")
elif imp == "2":
    if var == "1" or var == "2":
        harryexer(var)
    else:
        print("You choose something wrong, Please choose correct order ")
else:
    print("You choose something wrong, Please choose correct order ")

f1.close()
f2.close()
