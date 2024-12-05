import random # Импортирую рандом для генерации рандомных чисел в массив

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruits = ["apple", "banana", "watermelon", "cucumber"]

def numbers(numlist): # Функция удаляет каждую четную позицию перебором через цикл
    for i in numlist:
        x = i
        numlist.remove(x)
        i += 2
    print("\n" "Задание 1. Нечетные числа от 1 до 10 это:" "\n" f"{numlist}" "\n")

def fruiters(fruits): # Функция сортирует от наибольшего количества символов в строке к наименьшему
    fruits.sort(reverse=True)
    print("Задание 2. Сортировка строк в списке по убыванию символов:" "\n" f"{fruits}")

def summa(): # Функция суммирует все нечетные числа из рандомно генерируемых 10 чисел
    nlist = [] # Создается пустой массив
    for a in range(10): # Цикл заполняет массив рандомными 10 числами с значениями от 1 до 10
        nlist.append(random.randint(1, 10))
        a =+ 1
    answer = sum(nlist[::2]) # Метод sum суммирует каждую нечетную позицию
    print("\n" "Задание 3. Сумма чисел нечетных индексов из рандомных 10" "\n" f"{nlist}" "\n" f"{answer}")

numbers(numlist)
fruiters(fruits)
summa()