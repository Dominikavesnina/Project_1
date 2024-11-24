import datetime
import random
import secrets
import string


def generate_password(n, use_punctuation=False):
    """Генерация пароля заданной длины.

    Args:
        n (int) - длина пароля
        use_punctuation (bool, optional): опциональный параметр, определяющий
        нужно ли использовать спец.символы '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        в пароле. По-умолчанию выключен (имеет значение False).

    Returns:
        password: пароль в виде списка символов
    """
    alphabet = string.ascii_letters + string.digits
    if use_punctuation:
        alphabet += string.punctuation
    password = []
    for i in range(n):
        password.append(secrets.choice(alphabet))

    return password


n = int(input("Введите длину пароля:"))

password = generate_password(n, use_punctuation = False)
t = datetime.datetime.now()  # получаем текущее время
random.seed(t.microsecond)  # устанавливаем начальное состояние генератора случайных чисел

random.shuffle(password)  # случайным образом переставляем символы пароля

password_str = "".join(password)
print(f"Сгенерирован пароль: {password_str}")
# 7 - 26 строки - Веснина Доминика
# 29 - 38 строки - Медведева Ксения
