alfabeth = " абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def main():
    n = input("Введите номер желаемой буквы русского алфавита (от 1 до 33): ")

    try:
        is_n_int = int(n)
        n = int(n)

        def char(n):
            print(f"{n} буква алфавита, это {alfabeth[n].upper()}.")

        if n > 33:
            print("В русском алфавите 33 буквы...")
            main()
        elif n < -33:
            print("В русском алфавите 33 буквы...")
            main()
        else:
            char(n)
    except ValueError:
        print("Вы не ввели нужное число...")
        main()

def restart():
    answer = input("\n" "Продолжаем? (да/нет): ").lower()
    return answer == "да"

while True:
    main()
    if not (restart()):
        print("\n" "Завершение программы.")
        input("Нажмите Enter для выхода...")
        break
    else:
        print("Продолжаем..." "\n")