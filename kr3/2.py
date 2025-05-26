import numbers


def mul(a, b):
    """
    Функция умножения двух чисел. Имеет практическую пользу при умножении целых чисел.
    Может давать неверный или неточный результат
    при использовании в качестве параметров чисел с плавающей точкой
    в связи с особенностями представления таких чисел.
    Вызывает TypeError, если хотя бы один из параметров a или b не является числом
    :param a: первый множитель
    :param b: второй множитель
    :return: результат умножения a * b
    """

    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        raise TypeError("Either a or b is not a number")

    return a * b

# Примеры использования
print(mul(1, 2)) # 2
print(mul(8, 12)) # 96
print(mul(1.234e-14, 5))  # expected: 6.17e-14, got: 6.169999999999999e-14
print(mul("abcd", []))  # TypeError
print(mul(3, "345"))  # TypeError
