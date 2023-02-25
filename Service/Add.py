from datetime import datetime
from Model.Note import Note

# Создает и заполняет заметку, в результате работы возвращает объект "заметка"
class Add():

    def add(count):  
        obj_note = Note(None, None, None, None) 
        obj_note.id = count
        obj_note.title = (input('Заголовок: \n'))
        obj_note.message = (input('Текст: \n'))
        obj_note.date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        return obj_note

