#Программа считает факториал из числа, введенного пользователем
import os

def main():
    number = input("Введите число из которого хотите получить факториал: ") #Пользователь вводит число
    n = number #Переменная n нужна чтобы корректно вывести 16 строку

    try: #Проверка, был ли введен int или str
        user_input_as_int = int(number)
        number = int(number)
        if number == 0: #Проверка на 0. Если введен 0 должно вывести 1
            print(f"Факториал равен 1")
        else:
            x = number
            x = x ** 2
            x = round(x ** 0.5)

            while x > 2: #Цикл, который и считает факториал
                x -= 1
                number = number * x
                print(number) #Вывод каждой итерации, чтобы было наглядно и красиво
            print(f"Факториал {n} равен {number}")

    except ValueError: #Была введена строка
        print("Вы ввели неверное число...")

def ask2restart():
    answer = input("Есть еще числа для подсчета? (да/нет): ").lower()
    return answer == "да"

while True:
    main()
    if not ask2restart():
        print("Программа завершена.")
        input("Введите Enter для выхода...")
        break
    else:
        print("Продолжаем...")