import sys
sys.path.insert(0, 'Model')
from Note import Note
from Printer import Printer


class Edit():

    def enter_note(list_notes: Note):
        p = Printer
        p.print_list_notes(list_notes)
        title_for_del = input('Выбирете заметку (по заголовку): \n')
        for obj in list_notes:
            if (obj.title == title_for_del):
                return obj
        else:
            print('Такой заметки не найдено!')

    def modify_title(obj: Note):
        add_title = input("Вветите новый заголовок: \n")
        obj.title = f'{add_title}'
        print('\nИзменения внесены!')

    def modify_message(obj: Note):
        add_message = input("Вветите текст: \n")
        obj.message = f'{obj.message} {add_message}'
        print('\nИзменения внесены!')



# n1, n2, n3 = Note(1, 'title1', 'message1', 'date1'), Note(2, 'title2', 'message2', 'date2'), Note(3, 'title3', 'message3', 'date3')

# lst_n = [n1, n2, n3]
# p = Printer

# e = Edit
# e.modify_title(e.enter_note(lst_n))
# p.print_list_notes(lst_n)