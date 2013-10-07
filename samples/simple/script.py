kg = float(answers['0'])
m = float(answers['1'])
fat_index = kg/(m*m)
fat_index_pow = 0
if fat_index>18 and fat_index < 24:
    fat_index_pow = 5
elif fat_index>25 and fat_index<30:
    fat_index_pow = 3
elif fat_index>31 and fat_index<35:
    fat_index_pow = 2
elif fat_index>36:
    fat_index_pow = 1
print resource['fat_index'] % resource['fat_index_pow_%s' % fat_index_pow]
