# f = open("aman.txt", "w")#replace all contain
# f.write("aman is a good boy\n")
# f.write("aman is a good boy\n")
#
# f.close()
# f = open("aman.txt", "a")  # add after contain
# # f.write("aman is a good boy\n")
# a = f.write("aman is a good boy\n")
# print(a)
# f.close()
# Handle read and write both
f = open("aman2.txt", "r+")
print(f.read())
f.write("aman is good\n ")

f.close()
