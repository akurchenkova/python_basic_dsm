# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

user_name = input('Здравствуйте! Как вас зовут? ')
print(f'{user_name}! Добро пожаловать в систему КЭП. Я - капитан очевидность, \n'
      f'часто задаю неуместные вопросы и даю непрошенные советы, '
      f'ко всему прочему ещё и не всегда вежлив и толерантен.\n'
      f'Пожалуйста, не воспринимайте меня сербезно, я программа '
      f'и создан лишь для отработки навыков программирования моего создателя.')
year = int(input(f'Какой сейчас год? '))

while True:
    month = input(f'{user_name}, напишите, какой месяц по счету сейчас идёт? ')
    if month.isdigit():
        month = int(month)
        break
    print('Ошибка ввода. Надо ввести число.')
year_part = month / 12
print('Ого! значит уже %.2f года прошло. Нам надо ускориться.' % year_part)
user_age = int(input(f'{user_name}, Сколько вам полных лет? '))
print('Вот это да! Вы появились на свет в далеком', year - user_age, 'году.')
have_child = input('У вас есть ребенок? Ответ напишите да или нет: ')
if have_child == 'да':
    child_name = input('Как зовут вашего ребенка? ')
    child_age = int(input('Сколько лет вашему ребенку? '))
    print(f'Вот мы и познакомились поближе! {user_name}, теперь я знаю, '
          f'что ваш ребенок {child_name} родился, когда вам было {user_age - child_age}.')
elif have_child == 'нет':
    if user_age >= 28:
        print(f'{user_name}! В {user_age} уже лет можно создавать детей. '
              f'Хотите, чтобы я подобрал вам пару для этого или сначала хотите пройти курсы?')
    elif 18 <= user_age < 28:
        print(f'{user_name}! Понимаю, сначала карьера и деньги. '
              f'Хотите, чтобы я подобрал вам работу для этого?')
    elif 16 <= user_age <= 17:
        print(f'{user_name}, Согласен, сначала стоит получить образование. '
              f'Хотите, чтобы я подобрал вам университет?')
    else:
        print(f'{user_name}! В {user_age} слишком рано думать о детях. '
              f'Вы уже выбрали кем хотите стать в будущем?'
              f'Хотите, чтобы я подобрал вам подходящую профессию?')
else:
    print('Ошибка ввода. Вы не умеете выполнять четко поставленные задачи. Прощайте!')
