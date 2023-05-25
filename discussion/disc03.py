# recutsion
def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)


def merge(n1, n2):
    if n1 == 0 and n2 == 0:
        return 0
    elif n1 % 10 >= n2 % 10:
        if n2 != 0:
            return 10 * merge(n1, n2 // 10) + n2 % 10
        else:
            return 10 * merge(n1 // 10, 0) + n1 % 10
    else:
        if n1 != 0:
            return 10 * merge(n1 // 10, n2) + n1 % 10
        else:
            return 10 * merge(n1, n2 // 10) + n2 % 10


def make_func_repeater(f, num):
    def repeat(count):
        if count == 0:
            return num
        else:
            return f(repeat(count - 1))

    return repeat


from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    flag = int(sqrt(n))

    def prime_helper(divisor):
        if divisor <= flag:
            if n % divisor == 0:
                return False
            else:
                return prime_helper(divisor + 1)
        else:
            return True
    return prime_helper(2)
