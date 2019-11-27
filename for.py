"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def get_school_average(school_journal):
    all_scores = []
    for entry in school_journal:
        all_scores += entry['scores']
    return sum(all_scores)/len(all_scores)

def print_classes_average(school_journal):
    for entry in school_journal:
        print( 'Class:', entry['school_class'] )
        print( 'Average:', sum(entry['scores'])/len(entry['scores']) )

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_journal = [ {'school_class': '1A', 'scores': [3,5,4,4,4,4,2]} ]
    school_journal.append( {'school_class': '2B', 'scores': [4,3,3,4,5]} )
    school_journal.append( {'school_class': '3G', 'scores': [3,3,3,3,3]} )
    school_journal.append( {'school_class': '4A', 'scores': [2,1,5,3,2]} )

    print('School average:', get_school_average(school_journal) )
    print_classes_average(school_journal)

    
if __name__ == "__main__":
    main()
