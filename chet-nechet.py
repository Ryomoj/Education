#Программа запрашивает число и дает ответ - четное оно или нет
import os
def main():
	a = input("Введите целое число для проверки на четность: ")

	try: #Проверка на инт число
		c = int(a)
		b = int(a) % 2
		if b == 0:
			print("Вы ввели четное число!")
		elif b != 0:
			print("Вы ввели нечетное число!")

	except ValueError:
		print("Вы не ввели нужное число...")

def ask2restart():
	answer = input("Есть еще числа на проверку? (да/нет): ").lower()
	return answer == "да"

while True:
	main()
	if not ask2restart():
		print("Программа завершена.")
		input("Нажмите Enter для выхода...")
		break
	else:
		print("Продолжаем...")
