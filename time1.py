import time

# initial = time.time()
# print(initial)
# i = 0
# while i < 45:
#     print("My name is aman\n")
#     i += 1
# print("While loop run in", time.time() - initial, " sec")
#
# initial2 = time.time()
# for j in range(45):
#     print("My name is aman")
#     time.sleep(0.5)
# print(f"for loop run in {time.time() - initial2} sec")
i = 0
while i < 100:
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    time.sleep(1)
    i += 1
