# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, year, city, email, phone):
    """
    Тут могло бы быть описание функции
    ver1

    """
    return ' '.join([name, surname, year, city, email, phone])


def user_info(**kwargs):
    """
    Тут могло бы быть описание функции
    ver2

    """
    for info, i in kwargs.items():
        print(kwargs.get(info, " "), end=" ")


def my_function(**kwargs):
    """
    Тут могло бы быть описание функции
    ver3

    """
    name = kwargs.get("name")
    surname = kwargs.get("surname")
    year = kwargs.get("year")
    city = kwargs.get("city")
    email = kwargs.get("email")
    phone = kwargs.get("phone")
    return f"\n{name} {surname} {year} {city} {email} {phone} "


print(my_func(name="Семен", surname="Соколов", year="1989", city="Москва", email="mail@mail.ru", phone="79097090077"))
user_info(name="Иван", surname="Петров", year=1988, city="Москва", email="mail@gmail.ru", phone=79007007770)
print(my_function(name="Павел", surname="Воробьев", year="1997", city="Москва", email="mail3@mail.ru", phone="79097098898"))




