import os


def system(path, fileN, forma):
    path = path
    fileN = fileN
    os.chdir(path)
    with open(fileN) as fi:
        var = fi.read()
    count = 1
    for i in os.listdir():
        Name, Forma = os.path.splitext(i)
        if Forma == f".{forma}":
            newname = f"{str(count)}{Forma}"
            count += 1
            os.rename(i, newname)
        elif Name not in var:
            ti = Name.title()
            Newname = f"{ti}{Forma}"
            os.rename(i, Newname)
        else:
            Newname = f"{Name}{Forma}"
            os.rename(i, Newname)


p = input("path: ")
f = input("file name: ")
e = input("fileformat: ")
system(p, f, e)
