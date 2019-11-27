"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    q_and_a = {'How are you?': 'Just fine!', 'What are you doing?': 'Working', 'How old are you?': '100500',
               'Where do you come from?': 'Neverland', 'Where are you going?': 'Nowhere'}
    while True:
        q = input('Your question: ')
        if 'Goodbye'==q or 'bye'==q:
            print('Goodbye!')
            break
        a = q_and_a.get(q,0)
        if not a==0:
            print(a)
        else:
            print('I don\'t know the answer')
    
if __name__ == "__main__":
    ask_user()
