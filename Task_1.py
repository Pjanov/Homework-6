# Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200.
# Использовать comprehensions

n = int(input('Введите число N: '))
res = [i for i in range(n) if i % 2 == 1 and i*i < 200]
print(res)
