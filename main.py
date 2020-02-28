#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    sum = x + y
    return sum


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    product = 0
    if y >= 0:
        for i in range(y):
            product = add(product, x)
    else:
        for j in range(-y):
            product -= x
    return product


def power(x, n):
    """Raise x to power n, where n >= 0"""
    result = x

    if n >= 0:
        nums = range(1, n)
        for i in nums:
            result = multiply(result, x)
    return result

print(power(-2, 4))



def factorial(x):
    """Compute factorial of x, where x > 0"""
    result = 1
    for i in range(1, x + 1):
        result = multiply(result, i)
    return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    num_list = [0, 1, 1]
    for i in range(2, n):
        num_list.append(num_list[-1] + num_list[-2])
    return num_list[n-1]


if __name__ == '__main__':
    # your code to call functions above
    pass
