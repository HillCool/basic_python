#!/usr/bin/env python3
# )list和type的使用
# ---------------- list ----------------
# init
class_list = ['hyj', 'lhh']
print(class_list[0])
print(len(class_list))
print(class_list[-1])
# print(classlist[10]) #ERROR

# insert element
len = len(class_list)
class_list.insert(len, 'lhl')
print(class_list)

# delete element
class_list.pop()
print(class_list)
class_list.pop(1)
print(class_list)

# update element
class_list[0] = 'wuyifan'
print(class_list)

# ---------------- tuple ----------------
class_mate = ('hyj', 'lhh')
print(class_mate)
test = (1,)
print(test)

# ---------------- exercise ----------------
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 请用索引取出下面list的指定元素：
# # 打印Apple:
# print(?)
# # 打印Python:
# print(?)
# # 打印Lisa:
# print(?)
print(L[0][0])
print(L[1][1])
print(L[2][2])
