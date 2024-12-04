#Программа генерирует 10 рандомных чисел от 1 до 100 и выводит максимальное из них число
import os
import random #Для генерации рандомных чисел в массив импортируется этот модуль

def main():
    numlist = []

    count = 0
    while count < 11: #Генерируем рандомные числа от 1 до 100, они запихиваются в массив
        numlist.append(random.randint(1, 100))
        count += 1
    max_number = numlist[0]

    for i in numlist: #Проверяем каждое число и записываем самое большое в переменную max_number
        if i > max_number:
            max_number = i

    print(numlist) #Вывод массива для наглядности
    print(f"Максимальное число: {max_number}") #Вывод ответа

def ask2restart():
    answer = input("Хотите продолжить проверку? (да/нет): ").lower()
    return answer == "да"

while True:
    main()
    if not ask2restart():
        print("Программа завершена.")
        input("Введите Enter для выхода...")
        break
    else:
        print("Продолжаем...")
