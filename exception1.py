"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    q_and_a = {'How are you?': 'Just fine!', 'What are you doing?': 'Working', 'How old are you?': '100500',
               'Where do you come from?': 'Neverland', 'Where are you going?': 'Nowhere'}
    while True:
        try:
            q = input('Your question: ')
            a = q_and_a.get(q, 0)
            if not a == 0:
                print(a)
            else:
                print('I don\'t know the answer')
        except KeyboardInterrupt:
            print('Bye-Bye')
            break

    
if __name__ == "__main__":
    ask_user()
