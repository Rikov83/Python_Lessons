# Функции часть 1. Домашнее задание.

# Задача 1
# Напишите функцию, которая берёт на вход строку и возвращает true,
# если она является палиндромом и false в противном случае.

print("Task1 - Palindrome")


def palindrome(text):
    text1 = text.replace(" ", '')
    text2 = text1[::-1]

    if text1.lower() == text2.lower():
        return text2.lower(), True
    else:
        return text2.lower(), False


print(palindrome(input("введите текст на проверку палиндрома: ")))

# Задача 2
# Напишите и вызовете для себя или какого-нибудь персонажа функцию,
# которая берёт на вход имя, фамилию, отчество и возраст и возвращает
# строку вида “Иванов Иван Иванович 1973 г.р. зарегистрирован”.


print("Task2 - Demo info")


def demo_data(name, last_name, middle_name, year_birth):
    demo_info = last_name + ' ' + name + ' ' + middle_name + ' ' + year_birth + ' г.р. зарегистрирован'
    return demo_info

print(
    demo_data('Sergey','Rykov','Sergeevich',
              '1983'))  # Default sample
print(
    demo_data(input("введите имя: "), input("введите фамилию: "), input("введите отчество: "),
              input("введите г.р.: ")))  # sample for input

# Задача 3
# Напишите функцию, которая берёт на вход 2 или 3 натуральных числа
# и возвращает их максимум. Встроенным методом max() пользоваться
# нельзя. Возможно, вам потребуется указать аргумент по умолчанию.

print("Task3 - max from natural numbers")


def max_data(n1, n2, n3=0):
    if n1 >= n2 and n1 >= n3:
        return print(f'Максимальное число: {n1}')
    elif n2 >= n1 and n2 >= n3:
        return print(f'Максимальное число: {n2}')
    else:
        return print(f'Максимальное число: {n3}')


print(max_data(int(input("введите число1: ")), int(input("введите число2: "))))  # для 2x чисел
print(
    max_data(int(input("введите число1: ")), int(input("введите число2: ")),
             n3=int(input("введите число3: "))))  # для 3х чисел
