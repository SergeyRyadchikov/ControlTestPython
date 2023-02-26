from Model.Note import Note


class Save():

    def __init__(self, file, file_count):
        self.file = file
        self.file_count = file_count

    def save_parameters(self, list_notes: Note, count: int):  
        for obj in list_notes:
            with open(self.file, 'r', encoding='utf-8'), open(self.file, 'w', encoding='utf-8') as f:
                f.writelines(f'{obj.id};{obj.title};{obj.message};{obj.date_time}')
                f.writelines('\n')
            with open(self.file_count, 'r', encoding='utf-8'), open(self.file_count, 'w', encoding='utf-8') as k:
                k.write(count)


