class NegativeNumberError(Exception):
    def __init__(self, message="Число не может быть отрицательным"):
        self.message = message
        super().__init__(self.message)

def check_number(x):
    if x < 0:
        raise NegativeNumberError("Ошибка: введено отрицательное число!")
    return x

try:
    check_number(-5)
except NegativeNumberError as e:
    print(e)
else:
    print("Всё ахуенно!")