# -*- coding: utf-8 -*- 
a = answers
res = resources
kg = float(a['0'])
m = float(a['1'])
m = m / 100.0
fat_index = kg / (m * m)
fat_index_pow = 0
if fat_index > 18 and fat_index < 24:
    fat_index_pow = 0
elif fat_index > 25 and fat_index < 30:
    fat_index_pow = 1
elif fat_index > 31 and fat_index < 35:
    fat_index_pow = 2
elif fat_index > 35 and fat_index < 40:
    fat_index_pow = 3
elif fat_index > 40:
	fat_index_pow = 4
if fat_index_pow == 0:
	print res['fat_index_pow_0']
else:
	print res['fat_index'] % res['fat_index_pow_%d' % fat_index_pow]

i = 1
# 1
r = a[str(i)]
i = i + 1
print

# 2
r = 0
for x in xrange(i, i + 10):
    r = r + int(a[str(x)])
    i = i + 1
r = r / 100
if r > 12 and r < 26:
    print res['a2_1']
elif r > 26 and r < 30:
    print res['a2_2']
elif r > 30 and r < 35:
    print res['a2_3']
print

# 3
r = 0
for x in xrange(i, i + 8):
    r = r + int(a[str(x)])
    i = i+ 1
r = r / 80
if r > 18 and r < 24:
    print res['a3_1']
elif r > 24 and r < 30:
    print res['a3_2']
elif r > 30 and r < 35:
    print res['a3_3']
print

# 4
r = 0
for x in xrange(i, i + 4):
    r = r + int(a[str(x)])
    i = i+ 1
r = r / 40
if r > 16 and r < 20:
    print res['a4_1']
elif r > 21 and r < 32:
    print res['a4_2']
    
# 5
r = 0
for x in xrange(i, i + 7):
    r = r + int(a[str(x)])
    i = i+ 1
r = r / 40
if r > 15 and r < 22:
    print res['a5_1']
elif r > 23 and r < 31:
    print res['a5_2']
elif r > 32:
    print res['a5_3']

