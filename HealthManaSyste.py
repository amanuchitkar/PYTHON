f1 = open("nayanFood.txt", "a")
f2 = open("nayanExe.txt", "a")


def getdate():
    import datetime
    return datetime.datetime.now()


t = getdate()


def nayanfood(var1):
    if var1 == "1":
        inp = input("What Nayan Eat:")
        f = open("nayanFood.txt", "a")
        f.write(str(t))
        f.write(" : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var1 == "2":
        f = open("nayanFood.txt", "rt")
        r = f.read()
        print(r)
        f.close()
    else:
        print("You choose something wrong, Please choose correct order ")

print("Choose a person")
print("1.Nayan\n2.Aman")
per = input(": ")
print("For what: ")
print("1.Food\n2.Exersice")
cho = input(": ")
print("1.Log\n2.Retrive")
var = input(": ")
if per == "1":
    if cho == "1":
        if var == "1" or var == "2":
            nayanfood(var)

f1.close()
f2.close()
