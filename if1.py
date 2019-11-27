"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def age_to_profession(age):
    profession = ''
    if age < 6:
        profession = 'Kindergarten'
    elif age < 17:
        profession = 'School'
    elif age < 23:
        profession = 'University'
    else:
        profession = 'Employment'
    return profession

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_age = int(input('Your age: '))
    profession = age_to_profession(user_age)
    print(profession)

if __name__ == "__main__":
    main()
