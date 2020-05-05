#!/usr/bin/env python3
# 切片

L = ['hyj', 'lhh', 'hello']
print(L[0:2])

L2 = list(range(100))
print(L2[:10])
print(L2[-10:])
print(L2[10:20])
print(L2[:10:2])
print(L2[::2])

T = (0, 1, 2, 3, 4, 5)
print(T[:3])

# ---------------- iteration ----------------
# from collections import Iterable ## abandon

from collections.abc import Iterable

print(isinstance('abc', Iterable))

# ---------------- list generator ----------------

L2 = [x * x for x in list(range(1, 11))]
print(L2)

# ---------------- list generator ----------------
g = (x * x for x in range(10))
for n in g:
    print(n)


# ---------------- exercise ----------------
def trim(x):
    if x == '':
        return x
    else:
        if x[0] == ' ':
            return trim(x[1:])
        elif x[-1] == ' ':
            return trim(x[:-1])
        else:
            return x


def test1():
    if trim('hello  ') != 'hello':
        print('测试失败!', trim('hello  '))
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')


def findMinAndMax(L):
    if isinstance(L, Iterable) and L != []:
        max = L[0]
        min = L[0]
        for num in L[1:]:
            if num >= max:
                max = num
            elif num <= min:
                min = num
            else:
                pass
        return (min, max)
    else:
        return (None, None)


def test2():
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败1!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败2!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败3!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败4!')
    else:
        print('测试成功!')


# test2()

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L1 = ['Hello', 'World', 18, 'Apple', None]
T2 = [item.lower() for item in L1 if isinstance(item, str)]


def test3():
    print(T2)
    if T2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败222!')


test3()
