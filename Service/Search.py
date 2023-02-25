from Model.Note import Note

class Search():

    def search_note(list_notes: Note):
        title_for_del = input('Введите заголовок для поиска: \n')
        for obj in list_notes:
            if (obj.title == title_for_del):
                return obj
            else:
                print('Такой заметки не найдено!')