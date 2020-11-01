# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    user_num = input('Введите целое положительное число: ')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print('Ошибка ввода. Надо ввести целое положительное число.')

max_num = 0
while user_num and max_num != 9:
    tmp = user_num % 10
    if tmp > max_num:
        max_num = tmp
    user_num = user_num // 10
print(max_num)
