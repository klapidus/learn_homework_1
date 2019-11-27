"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def compare_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    if str1==str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif 'learn'==str2:
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    # str1 = input('string1: ')
    # str2 = input('string2: ')
    print ( compare_strings(123, {'key1': 'value1', 'key2': 'value2'} ) )
    print ( compare_strings('privet','privet') )
    print ( compare_strings('privet hello','privet') )
    print ( compare_strings('hi','learn') )


if __name__ == "__main__":
    main()
