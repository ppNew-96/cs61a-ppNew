# High Order Function
# Functions that manipulates other functions by taking in function as arguments.

def keep_ints(cond, n):
    num = 1
    while num <= n:
        if cond(num):
            print(num)
        num += 1


def make_keeper(n):
    def func(cond):
        num = 1
        while num <= n:
            if cond(num):
                print(num)
            num += 1

    return func


def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)

    return delay_print


def print_n(n):
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print
