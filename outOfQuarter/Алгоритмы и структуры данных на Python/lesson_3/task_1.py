#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
for i in range(2,10):
    _count = 0
    for num in range(2,99):
        if num % i == 0:
            _count += 1
    print(f'"{i}" кратно {_count} чисел')