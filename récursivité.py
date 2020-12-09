import random


def addition(n, acc=1):
    if n == 1:
        return acc
    else:
        return addition(n - 1, acc + n)


# print(addition(5))

def euclide(a, b):
    if 0 < a % b < b:
        return euclide(b, a % b)
    else:
        return b


# print(euclide(502, 2))

def fibo(n):
    if 1 >= n:
        return n
    else:
        return fibo(n-1) +fibo(n-2)



#print(fibo(9))
