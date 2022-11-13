import argparse
import sys


def calc(arg):
    if arg.o == "add":
        return arg.x + arg.y
    elif arg.o == "sub":
        return arg.x - arg.y
    elif arg.o == "mul":
        return arg.x * arg.y
    elif arg.o == "div":
        return arg.x / arg.y
    else:
        return "inapropriat input!!!!!"


def fulty_calc(arg):
    if arg.o == "add":
        if arg.x == 56 and arg.y == 9 or arg.x == 9 and arg.y == 56:
            return "77"

        else:
            return arg.x + arg.y
    elif arg.o == "sub":
        return arg.x - arg.y
    elif arg.o == "mul":
        if arg.x == 45 and arg.y == 3 or  arg.x == 3 and arg.y == 45:
            return "555"
        else:
            return arg.x*arg.y
    elif arg.o == "div":
        if arg.x == 56 and arg.y == 6:
            return "4"
        else:
            return arg.x/arg.y
    else:
        print("inapropriat input!!!!!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0, help="fir se try kar")
    parser.add_argument("--y", type=float, default=1.0, help="fir se try kar")
    parser.add_argument("--o", type=str, default="add", help="fir se try kar")
    arg = parser.parse_args()
    sys.stdout.write(str(fulty_calc(arg)))
