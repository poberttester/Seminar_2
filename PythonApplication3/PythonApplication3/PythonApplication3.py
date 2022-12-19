# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

'''
Пример:

-Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
Сумма 9.06

'''

n = 4
i = 1
summ = 0
result = 0
print('Для n=', n, '{', end=(''))
while i < n:
	result = round((1 + 1/i) ** i, 2)
	summ += result
	print(i,':', result, end=(', '))
	i += 1

result = round((1 + 1/n) ** n, 2)
summ += result
print(result, '}')

print(f'Сумма {summ}')

