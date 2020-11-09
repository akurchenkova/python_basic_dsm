"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


# Каждое слово состоит из латинских букв в нижнем регистре.
# ввод: nice авп ъghj jапро hjjпаро вапрghgh cool
# вывод: Nice Cool


def int_func(user_word):
    """
    Функция, принимающую слово(а) из маленьких латинских букв и возвращающую с прописной буквы.

    """
    for word in user_word.split():
        letters = 0
        for letter in word:
            if 97 <= ord(letter) <= 122:
                letters += 1
        if letters == len(word):
            print(word.capitalize(), end=" ")
            # еще есть .title(), но так как мы у каждого слова отдельно изменяем первую букву,
            # а не у предложения в целом, то я выбрала .capitalize()


user_sent = input('Введите слово или несколько слов через пробел из маленьких латинских букв:\n')
if not user_sent.islower():
    print("Ошибка ввода! Наша функция вредная и читает только маленькие буквы.\n"
          "Сохраню всем время и сама уменьшу буквы. Верный вариант написания для программы:")
    print(user_sent.lower())
    user_sent = user_sent.lower()

int_func(user_sent)

# int_func('text')
# int_func('nice авп ъghj jапро hjjпаро вапрghgh cool')
