# Задача 1. Нужно написать программу, которая бы вычисляла количество городов, названия которых повторяются.
# В первой строке указывается количество городов n, затем вводятся n строк с названиями городов.
# Ввод:
# 6
# Курск
# Калуга
# Анапа
# Анапа
# Абинск
# Курск
# Вывод: 4

print("Task1 - Number of doubled cities")
numb_of_cities = int(input("Введите кол-во городов: "))
cities = []

numb_of_duplicates: int = 0
while numb_of_cities < 1:
    print("введено неверное число. Попробуйте снова.")
    numb_of_cities = int(input("Введите кол-во городов: "))

for i in range(numb_of_cities):
    city = input(f'Город {i + 1}: ').strip().upper()
    cities.append(city)

    if cities.count(city) == 2:
        numb_of_duplicates += cities.count(city) # если дубль встретился впервые, то прибавляем 2
    elif cities.count(city) > 2: #если город встречается больше 2х раз то прибавляем 1
        numb_of_duplicates += 1

print(f'Список городов {cities}, из них повторяются {numb_of_duplicates}')

# решение через словари. Разбор с преподавателем
# lst = [1, 2, 3, 4, 5, 5, 3, 2]
# def = dict{}
# for e in lst: # проверяем что ключ есть в словаре
#     if e in dct:
#         dct[e] += 1
#     else:
#         dct[e] = 1
#
# for value in dct.values():


# Задача 2.Младшая сестра Фёдора - Соня пишет сочинение по литературе и отправляет файлы учительнице.
# Фёдор знает, что Соня никогда не ставит заглавные буквы, так как для набора текста использует компьютер.
# Пока никто не видит, Фёдор решил внести исправления в сочинение сестры и написал программу,
# которая восстанавливает заглавные буквы в строке.
# Программа работает по следующему алгоритму:
# * сделать заглавной первую букву в строке, не считая пробелы;
# * сделать заглавной первую букву после точки, восклицательного или вопросительного знака, не считая пробелы.
# Ввод: на этом заканчиваю свое сочинение. поставьте пятерку, Мария Ивановна! я очень старалась!
# Вывод: На этом заканчиваю свое сочинение. Поставьте пятерку, Мария Ивановна! Я очень старалась!

# решение: здесь нужно заново собрать строку. Задаем 0й символ по умолчанию как заглавный,
#          тк предложение всегда начинается с большой буквы. Далее создаем цикл for i in len(text)
#          и для каждого i проверяем не было ли (.!?) два символа назад. Если был, то делаем аппер для этого символа.
#          Для остальных присоединяем как есть. Учесть, что для второго символа
#          нет двух символов назад

print("Task2 - Upper letters in sentence")
sentence = "на этом заканчиваю свое сочинение. поставите пятерку, Мария Ивановна? я очень старалась! спасибо... мама."
print(sentence)
# sentence = int(input("Введите предложение: ")) # если нужен ручной ввод
new_sentence = sentence[0].upper() + sentence[1]
# print(new_sentence)  # проверка 1х двух символов
len_s = len(sentence)
for i in range(2, len_s):
    if sentence[i-2] in (".", "!", "?"):
        new_sentence += sentence[i].upper() # меняем букву на заглавную если два символа назад был (".", "!", "?")
        # print(new_sentence, sentence[i-2], i, len_s) # пошаговая проверка
    else:
        new_sentence += sentence[i]
        # print(new_sentence, sentence[i-2], i, len_s) # пошаговая проверка
print(f"Предложение с заглавными буквами: {new_sentence}")

# Задача 3.Проверка на анаграмму. Пользователь вводит две строки. Напишите программу, которая определяет,
# являются ли эти строки анаграммами (содержат одни и те же символы, но в разном порядке).
# Выведите соответствующее сообщение.
# Подсказка: воспользуйтесь множеством для сравнения уникальных символов в строке,
# но не забудьте избавиться от пробелов.
# вариант для проверки:
# Мир, играл в прятки!
# Игла, Ралли и тяпки вам!

print("Task3 - Anagramma check")
sent1 = input("Введите строку 1: ").lower().replace(" ", "")
# sent1 = "Строка 1: Готова".lower().replace(" ", "") #чтобы не придумывать текст
sent2 = input("Введите строку 2: ").lower().replace(" ", "")
# sent2 = "сократт: 1 твоРог".lower().replace(" ", "") #чтобы не придумывать текст

if set(sent1) == set(sent2):  # проверяем совпадают ли множества по символам
    print(f'Эти строки являются анаграммами: {set(sent1)} / {set(sent2)}')
else:
    print(f'Эти строки НЕ являются анаграммами: {set(sent1)} / {set(sent2)}')

# Задача 4. В олимпиаде по математике школьникам было предложено решить одну задачу по алгебре,
# одну по геометрии и одну по тригонометрии.
# Напишите программу, которая определяет, сколько учащихся решили все задачи.
# Формат ввода:
# На вход подается три строки:
# 	•	в первой строке указаны фамилии школьников, решивших задачу по алгебре;
# 	•	во второй строке указаны фамилии школьников, решивших задачу по геометрии;
# 	•	в третьей строке указаны фамилии школьников, которые решили задачу по тригонометрии.
# Формат вывода:
# Требуется вывести в алфавитном порядке через пробел фамилии учащихся,
# решивших все три задачи олимпиады. Если таких нет, вывести строку "Все три задачи никто не решил".
# Ввод:
# Иванов Петров Сидоров Михайлов
# Иванов Михайлов
# Сидоров Михайлов
# Вывод: Михайлов

print("Task4 - Olimpiada")

# alg = set('Якин Петров Сидоров Михайлов'.split())     # для использования без ручного ввода
# geom = set('Якин Иванов Михайлов Сидоров'.split())    # для использования без ручного ввода
# trig = set('Сидоров Михайлов Якин'.split())           # для использования без ручного ввода
alg = set(input('Введите фамилии по алгебре: ').split())
geom = set(input('Введите фамилии по геометрии: ').split())
trig = set(input('Введите фамилии по тригонометрии: ').split())
winners = list(alg & geom & trig)   # проверяем пересечения в 3х множествах
winners.sort()
if alg & geom & trig == set():  # проверяем, если множество пустое, значит никто не решил
    print("Все три задачи никто не решил")
else:
    print('Список тех, кто решил все задачи:', *winners)



