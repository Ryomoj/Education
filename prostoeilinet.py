#Программа запрашивает ввод числа у пользователя и определяет простое оно или сложное
import os

def main():
    number = input("Введите целое число, и я проверю его на простоту:")

    try: #Проверка ввода на инт
        is_input_int = int(number)
        number = int(number)
        if number % 2 and number % 3 != 0: #Проверка на простое число
            print(f"Число {number} простое!")
        else:
            print(f"Число {number} сложное!")
    except ValueError:
        print("Вы не ввели нужное число...")

def ask2restart():
    answer = input("Есть еще числа для проверки? (да/нет): ").lower()
    return answer == "да"

while True:
    main()
    if not ask2restart():
        print("Программа завершена.")
        input("Нажмите Enter для выхода...")
        break
    else:
        print("Продолжаем...")