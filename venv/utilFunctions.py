#
import sys


class UtilFunctions:
    def __init__(self):
        pass

    def add_numbers(self, a, b):
        return a + b

    def subtract_numbers(self, a, b):
        return a - b


def main():
    util_functions = UtilFunctions()
    arg1 = float(sys.argv[1])
    arg2 = float(sys.argv[2])

    print('Numbers entered are ', arg1, ' and ', arg2)
    print('Numbers added are ', util_functions.add_numbers(arg1, arg2))
    print('Numbers subtracted are ', util_functions.subtract_numbers(arg1, arg2))


if __name__ == "__main__":
    main()