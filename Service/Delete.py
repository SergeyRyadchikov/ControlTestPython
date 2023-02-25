
from Model.Note import Note


class Delete():

    def instruction(list_notes: Note):
        title_for_del = input('Введите заголовок для удаления: \n')
        for obj in list_notes:
            if (obj.title == title_for_del):
                del obj
                print('Заметка успешно удалена!')
            else:
                print('Такой заметки не найдено!')
