
# Write a program that will calculate the number
# of trailing zeros in a factorial of a given number.

def zeros(n):
    res = 0
    while n != 0:
        n = n // 5
        res += n
    return res