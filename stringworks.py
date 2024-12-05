input_name = input("Введите имя: ").lower()
input_surname = input("Введите фамилию: ").lower()

name = input_name[0].upper() + input_name[1::]
surname = input_surname[0].upper() + input_surname[1::]
welcome_phrase = "Добро пожаловать"

def welcome(name, surname):
    print("\n" f"{welcome_phrase}, {surname} {name}!")

welcome(name, surname)

def ask():
    answer = input("\n" "Хотите изменить приветствие? (да/нет) ").lower()
    return answer == "да"

while True:
    if not (ask()):
        input("Нажмите Enter для завершения...")
        break
    else:
        phrase = input("Введите другое приветствие: ")
        welcome_phrase = phrase
        welcome(name, surname)


