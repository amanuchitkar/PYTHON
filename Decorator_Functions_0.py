def dec1(func1):
    def nowexe():
        print("Executing Now")
        func1()
        print("Executed")

    return nowexe

@dec1
def Who_is_aman():
    print("aman is a good boy.")
# Who_is_aman = dec1(Who_is_aman)


Who_is_aman()
