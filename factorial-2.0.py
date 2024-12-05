import os

def main():
    number = input("Введите целое число, а я вычислю факториал: ")

    try:
        is_input_int = int(number)
        number = int(number)

        def factorial(number):
            n = number ** 2
            n = n ** 0.5

            if n == 0:
                return 1
            else:
                return round(number * factorial(n-1))

        factorial(number)

        def print_answer():
            print(factorial(number))
        print_answer()
    except ValueError:
        print("Вы не ввели верное число...")
        main()

def ask2restart():
    answer = input("Есть еще числа для вычисления? (да/нет): ").lower()
    return answer == "да"

while True:
    main()
    if not ask2restart():
        print("Программа завершена.")
        input("Введите Enter для выхода...")
        break
    else:
        print("Продолжаем...")