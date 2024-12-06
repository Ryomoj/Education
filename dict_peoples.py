peoples = dict(Артем=22, Наташа=23, Женя=21, Катя=24, Макс=17, Лена=54)

for key, value in peoples.items(): # Цикл выводит имя и возраст каждого человека в списке
    print(key, value)

def find_age(): # Функция для поиска человека по имени и вывода его возраста
    name = input("Введите имя человека: ")
    value = peoples.get(name)
    print("Запрашиваемый возраст: " f"{value}")

def main(): # Функция меню
    answer = input("\n" "Найдем возраст по имени или выйдем? (найти/выйти)").lower()
    if answer == "найти":
        find_age()
        main()
    elif answer == "выйти":
        input("Нажмите Enter для выхода...")
        exit()
    else:
        print("Неверный ввод...")
        main()

main()


