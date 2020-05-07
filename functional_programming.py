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


def by_score(t):
    return t[-1]


def test5():
    L2 = sorted(L, key=by_name, reverse=true)
    print(L2)
    L3 = sorted(L, key=by_score, reverse=true)
    print(L3)


# test5()
# ------------------------- function programming advance--------------------------
##返回函数
# 闭包 (难点)
# 1、来理解
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    print(i)  # 在这里把这个log打出来，就清晰了
    return fs


def test1():
    f1 = count1()
    print(f1)
    for f in f1:
        print(f())


# test1()

# 2、修改一把
def count2():
    fs = []
    for i in range(1, 4):
        def f(i2):
            print(i2)  # 看，我把i当参数传进来了，保存在了f函数，作为局部变量了，直接算出结果了。
            return i2 * i2

        fs.append(f(i))
    return fs


def test2():
    f1 = count2()
    print(f1)


# test2()

# 3、再修改一把
def count3():
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


def f(i):
    return i ** 2


def test3():
    f1 = count3()
    print(f1)


# test3()

# 2、3 结果一毛一样

# 4、再修改一把
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


def test4():
    f1 = count
    f2 = count
    f3 = count
    print(f1())
    print(f2())
    print(f3())


# 匿名函数
list(map(lambda x: x * x, [1, 2, 3]))

# 装饰器
import functools


def log(func):
    @functools.wraps(func)  # try delete raw
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


print(now.__name__)
now()

# 偏函数
int2 = functools.partial(int, base=2)
print(int2('1000000'))


# exercise
# 6. 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def nums():  ##无限自然数
    n = 0
    while True:
        n = n + 1
        yield n


def createCounter():
    it = nums()

    def counter():
        return next(it)

    return counter


# 测试:
def test6():
    counterA = createCounter()
    l = []
    a = nums()
    # for n in list(range(1, 100)):
    #     l.append(next(a))
    # print(l)
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')


test6()

# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))


def test7():
    print(L)


test7()

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time


def metric(Text):
    def do_metric(fn):
        @functools.wraps(fn)
        def wrapper(*args):
            t1 = time.time()
            res = fn(*args)
            t2 = time.time()
            print('%s %s executed in %s ms' % (Text, fn.__name__, t2 - t1))
            return res

        return wrapper

    return do_metric


# 测试
@metric("这是个快函数")
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric("这是个慢函数")
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


def test8():
    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')


test8()
