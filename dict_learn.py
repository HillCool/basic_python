#!/usr/bin/env python3
# ---------------- dict ----------------
d = {'wyf': 18, 'lyf': 10, 'wsc': 8}
print(d['wyf'])
d['wsc'] = 11
print(d['wsc'])
# only one value,the following will overwrite
d['wsc'] = 12
print(d['wsc'])
# non-exists will error
# print(d['hyj'])
# to avoid key is non-exists, using get
print(d.get('wyf'))
print(d.get('hyj'))

# delete element from dict
d.pop('wsc')
print(d)

# in python, change the key of dict is forbidden, list can not be a key also


# ---------------- set ----------------
# set only save key ,not value
s = set([1, 2, 3])
print(s)
