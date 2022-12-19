# Программа принимает на вход вещественное число и показывает сумму его цифр.

def sum_of_digits(num):
		
		summ = 0
		numb_str = str(num) 

		if numb_str.find(".") != -1:
			splits = numb_str.split(".")
			firstNumb = int(splits[0])
			secondNumb = int(splits[1])						

			while firstNumb > 0:
				summ = summ + firstNumb % 10
				firstNumb = firstNumb // 10
			while secondNumb > 0:
				summ = summ + secondNumb % 10
				secondNumb = secondNumb // 10
		else:
			numb_int = int(num)
			while numbs > 0:
				summ += numbs % 10
				numbs //= 10

		print("Сумма равна: ", summ)
		
	

someNumber = float(input("Введите число для расчёта суммы его цифр: "))

sum_of_digits(someNumber)




