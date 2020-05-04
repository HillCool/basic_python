#!/usr/bin/env python3
# 函数的使用
# ---------------- function basic ----------------
# function use
def basic():
    res = abs(-20)
    print(res)
    # data type change
    res1 = int('123')
    print(res1)
    print(hex(255))


# print(basic())
# ---------------- function init ----------------
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("wrong arg motherfucker")
    else:
        if x > 0:
            return x
        else:
            return -x


# print(my_abs(-20))
# print(my_abs('a')) wrong test
# ---------------- blank function----------------
def blank():
    pass


import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def test_move():
    x, y = move(100, 100, 60, math.pi / 6)
    p = move(100, 100, 60, math.pi / 6)
    print(x, y)
    print(p)


# print(test_move())
# ---------------- default function----------------
def double(x):
    return x ** 2


def double(x, n=2):  # default arg is behind the key arg
    # def double(x, n):  # override before fucntion
    return x ** n


def defalut():
    print(double(1, 2))
    print(double(2))


print(defalut())


# notice
def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


# print ->
# ['END']
# ['END', 'END'
# when we use default function ,be careful that when the function init,python default set L to the address of the [],
# so if we use it again ,will see double 'END'

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# ---------------- changing arg function----------------
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 3, 5, 7))
nums = [1, 2, 3]
res = calc(*nums)
print(res)


# ---------------- key arg function----------------

# ---------------- exercise ----------------
#  ax^2+bx+c=0

def quadratic(a, b, c):
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return r1, r2


def exercise():
    if quadratic(2, 3, 1) != (-0.5, -1.0):
        print('测试1失败', quadratic(2, 3, 1))
    elif quadratic(1, 3, -4) != (1.0, -4.0):
        print('测试2失败', quadratic(1, 3, -4))
    else:
        print('测试成功')


# print(exercise())

# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, y):
#     return x * y
def product(x, y, defalut=1):
    return x * y * defalut
