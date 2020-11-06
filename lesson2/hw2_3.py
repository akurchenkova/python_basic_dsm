"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

season_list = ['зима', 'весна', 'лето', 'осень']

season_dict = {'зима': (12, 1, 2),
               'весна': (3, 4, 5),
               'лето': (6, 7, 8),
               'осень': (9, 10, 11)}

while True:
    user_num = input('Введите номер месяца в виде целого числа от 1 до 12: ')
    if not user_num.isdigit():
        print('Ошибка. Введите число от 1 до 12: ')
    elif not 1 <= int(user_num) <= 12:
        print('Ошибка. Нужно ввести число от 1 до 12:')
    else:
        user_num = int(user_num)
        break

season_index = user_num // 3 % 4
season = season_list[season_index]
print(f"Решение через list: {user_num} месяц - {season}")

for key, value in season_dict.items():
    if user_num in value:
        print(f'Решение через dict: {user_num} месяц - {key}')
        break
