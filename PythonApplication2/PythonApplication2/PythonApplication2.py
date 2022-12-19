# Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.


N = int(input("Введите число: "))

i = 1
result = 1
print(f'\nпусть N = {N}, тогда [', end=(''))

while i < N:

	result *= i
	print(result, end=(', '))
	i += 1

result *= i
print(f'{result}]')