"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

sentence = input("Введите строку из нескольких слов, разделённых пробелами: ")
num_list = sentence.split()

for num, word in enumerate(num_list, 1):
    print(f'{num}. {word[:10]}')
