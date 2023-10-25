# Теоретическое задание: прочитать документацию о методах строк, списков и множеств.
#
# Задача 1.Вводится строка. Нужно превратить строку в список, разбив строку на слова и вывести список из слов, записанный в обратном порядке.
# Ввод:Death there mirth way the noisy merit
# Вывод:['merit', 'noisy', 'the', 'way', 'mirth', 'there', 'Death']
# Подсказка: вспомните, как работают срезы или метод reverse, изученный на занятии
# from typing import List

print("Task1 - sentence split and reversed")
print("введите предложение: ", end='')
sentence = input().split()
sentence.reverse()

print(sentence)


# Задача 2. Вводится строка из не менее 15 символов, программа выводит на экран символы с чётными номерами (нумерация с 0).
# Ввод: In the hole in the ground there lived a hobbit
# Вывод: I h oei h rudteelvdahbi
#        010101010101010101010101010101010101010101010

print("Task2 - choose every honest(четный) symbol from sentence")
print("введите предложение (не менее 15 знаков): ", end='')
sentence = input()

result = ''
while len(sentence) < 15:
    print("Предложение слишком короткое. Попробуйте снова")
    sentence = input("введите предложение (не менее 15 знаков): ")
for i in range(len(sentence)):
    if i % 2 == 0:
        result += sentence[i]
print(f'смотри какие символы здесь четные: {len(sentence)}, {result}')

# Задача 3.Вводится список чисел через пробел и натуральное число n - степень. Нужно возвести в заданную степень n все введенные числа.
# Желательно сделать, используя списочные выражения
# Ввод:3 5 -7 -13 43 8 0 -13 8 -1 2
# Вывод: [9, 25, 49, 169, 1849, 64, 0, 169, 64, 1]

print("Task3 - digits list and exponential")
lst = input("введите список чисел через пробел и степень для возведения: ").split()
lst_digit = [int(i) ** int(lst[-1]) for i in lst]  # переводим список в числовой формат и сразу возводим в степень последнего элемента
lst_digit.pop(-1)                                  # удаляем последний символ
exp = int(lst[-1])

print(f'результат возведения в {exp}-ю степень ранее введенных чисел: {lst_digit}')


# Задача 4. Вводится строка с текстом и символ. Требуется удвоить вхождение введённого символа в текст.
# Текст состоит из слов, записанных латинскими буквами через пробел, знаков препинания.
# Подсказка: вспомните, как работает метод replace
# Example
# string - "Following task looks unclear due to lack of input and output examples"
# symbol - u

print("Task4 - double marked symbol in sentence")
string = input("Введите текст на англ языке: ")
symbol = input("введите любой символ из предложения: ")
string_new = string.replace(symbol, symbol*2)

print(f'Обновленное предложение с задвоенным символом - {symbol}: {string_new}')

# Задача 5. Дана строка. Программа подсчитывает количество символов x и y и выводит строку вида "x: (число), y: (число)."
# Подсказка: вспомните метод count, изученный на занятии

print("Task5 - count of chosen letters 'x', 'y' in the string")
string2 = input("введите строку: ")

print(f' в данной строке букв x: {string2.count("x")}, y: {string2.count("y")}.')


# Задача 6.Вводится текст со сбалансированными скобками, программа выводит на экран текст без скобок и их содержимого.
# На пробелы и знаки препинания внимание не обращать, вложенных скобок в исходной строке нет.
# Подсказка: вспомните метод find, изученный на занятии.
# Ввод:When he saw Sally (a girl he used to go to school with) in the shop, he could not believe his eyes. She was fantastic (as always)!
# Вывод: a girl he used to go to school with
# as always

print("Task6 - print part of text in brackets")
# text = "When he saw Sally (a girl he used to go to school with) in the shop, he could not believe his eyes. She was fantastic (as always)!"
text = input("put the text: ")
print("Text in brackets: ")
for i in text:
    if i != '(':
        # print(i)
        continue
    else:
        text2 = text[text.find('(')+1:]     # обрезаем текст после первой найденной скобке "(", чтобы искать следующую
        print(text2[:text2.find(')')])
        text = text2
