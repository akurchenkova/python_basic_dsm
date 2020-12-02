"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

while True:
    user_num = input('Введите число n: ')
    if user_num.isdigit():
        break
    print('Ошибка ввода. Надо ввести целое положительное число.')
if 0 <= int(user_num) < 10:
    print(int(user_num) * 123)
else:
    result = int(user_num) + int(user_num * 2) + int(user_num * 3)
    print(result)
