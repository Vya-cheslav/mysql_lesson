# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

array = [64, 33, -96, 37, 38, 12, 45, -14, 47, 80, -49, 13, 79, -22, 25, 27, 93, 11]
_min1 = array[0]
_min2 = array[1]

for i in array:
    if i <= _min1:
        _min2 = _min1
        _min1 = i
    elif i <= _min2:
        _min2 = i

print(f'Два наименьших элемента {_min1} и {_min2}')