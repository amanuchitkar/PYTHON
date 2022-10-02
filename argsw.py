# def function_name(a, b, c, d, e):
#     print(a, b, c, d, e)
#
#
# function_name("aman", "shubham", "mrudul", "ashutosh", "nayan")

def funargs(normal, *args, **kwargs):
    print(normal)
    # print(type(args))
    for item in args:
        print(item)
    # print(args[1])
    print("Hamanre kuch chuninda chutiya logo se milia \n")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


# funargs("aman", "mrudul")
normal = "This is a normal line"

var = ["aman", "shubham", "mrudul", "ashutosh", "nayan", "latish"]

var1 = {"Mtudul": "topper", "aman": "Badmenton playar", "pranav": "ladkia patau",
        "anish": "chutiya", "ashutosh": "Chamia", "Nayan": "Bodybilder"}

funargs(normal, *var, **var1)
