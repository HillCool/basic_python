#!/usr/bin/env python3
# 条件判断
# ---------------- if ----------------
# age1 = input('age: ') #这里input的age1是一个str，所以下面用int去转换类型，但是如果遇到字符串在int处报错
# age = int(age1)
age = 20
if age > 20:
    print('# ---------------- exercise ----------------adult')
elif 10 < age < 20:  # 注意是elif不是elseif
    print('teen')
else:
    print('child')

x = 1  # 非零数值、非空字符串、非空list
if x:
    print('True')

# 练习 exercise
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
h = 1.75
w = 80.5
bmi = 80.5 / (1.75 ** 2)
if bmi < 18.5:
    print('过轻')
elif 18.5 < bmi < 25:
    print('正常')
elif 25 < bmi < 28:
    print('过重')
elif 28 < bmi < 32:
    print('肥胖')
elif 32 < bmi:
    print('严重肥胖')
