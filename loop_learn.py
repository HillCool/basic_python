#!/usr/bin/env python3
# 循环
# ---------------- loop ----------------
# basic
names = ['wyf', 'cwt', 'xz']
for name in names:
    print(name)
# basic2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for num in nums:
    sum = sum + num
print(sum)

num1s = list(range(101))  # 从0 开始
sum1 = 0
for num1 in num1s:
    sum1 = sum1 + num1
print(sum1)

# ---------------- while ----------------
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum2 = 0
num2 = 99
while num2 > 0:
    sum2 = sum2 + num2
    num2 = num2 - 2
print(sum2)
# ---------------- exercise ----------------
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
end = len(L)
start = 0
while start != end:
    print("Hello, %s!" % L[start])
    start = start + 1

for elm in L:
    print("Hello, %s!" % elm)
