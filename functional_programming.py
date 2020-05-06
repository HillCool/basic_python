#!/usr/bin/env python3

from functools import reduce


# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


# print(add(-5, 6, abs))


# map/reduce
def f(x):
    return x * x


def f2(x, y):
    return x * y


# r = map(f, [1, 2, 3, 4])
# print(r)
# print(list(r))
#
r2 = reduce(f2, [1, 2, 3, 4])


# print(r2)

# filter
def is_odd(n):
    return n % 2 == 1


# print(list(filter(is_odd, [1,2,3,4,5,6,6])))

# sorted


# function as return
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5)
f2 = lazy_sum(1, 3, 5)


# print(f)
# print(f())
# print(f2)
# print(f2())


# exercise
# 1.利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# lower() 小写、upper() 大写、capitalize()首字母大写、title()每个单词的首字母大写、swapcase()大小写互换
def normalize(name):
    first = name[0].upper()
    res = ''
    for char in name[1:]:
        res = res + char.lower()
    # return name.capitalize()
    return first + res


def test1():
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)


# test1()

# 2.Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    res = reduce(do_prod, L)
    return res


def do_prod(num, res):
    return num * res


def test2():
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')


# test2()

# 3利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    return reduce(reduce_str2float, map(map_str2float, s))


def map_str2float(s):
    if s == '.':
        pass
    else:
        int(s)


def reduce_str2float(s):
    pass


def test3():
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')


# 4回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    sn = str(n)
    l = len(sn)
    # print(sn, l)
    if l <= 1:
        return 1 == 1
    elif l == 2:
        return sn[0] == sn[1]
    elif l % 2 == 0:
        tial = list(sn[int(l / 2): l])
        tial2 = list(reversed(tial))
        return list(sn[0:int(l / 2)]) == tial2
    else:
        return sn[0:int(l / 2)] == sn[int(l / 2 + 1): l]


def test4():
    # 测试:
    output = filter(is_palindrome, range(1, 10000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')


# test4()

# 5排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t


L2 = sorted(L, key=by_name, reverse=true)
print(L2)


def by_score(t):
    return t[-1]


L3 = sorted(L, key=by_score, reverse=true)
print(L3)
