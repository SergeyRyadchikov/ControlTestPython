from datetime import datetime
from random import randint as rnd
from Abstract_instruction import Abstract_instruction


class Add(Abstract_instruction):

    def __init__(self, file):
        self.file = file

    def instruction(self):  
        with open(self.file, 'a', encoding='utf-8') as f:
            value_title = (input('Заголовок: \n'))
            value_msg = (input('Текст: \n'))
            date_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            id = rnd(0, 10)
            f.writelines(f'{id},{date_time},{value_title},{value_msg}')
            f.writelines('\n')

obj_add = Add('C:\\Users\\Сергей\\Desktop\\GB\\Факультет Digital-master\\Промежуточная аттестация\\Python\\Заметки\\test.csv')
obj_add.instruction()   

