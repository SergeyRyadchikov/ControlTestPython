


class Printer():

    def print_note(obj):
        print(
            f'id={obj.id}, datatime={obj.date_time}\ntitle={obj.title}\nmessage={obj.message}\n')
        
    def print_list_notes(list_notes):
        for obj in list_notes:
            print(f'id = {obj.id}  |  title = {obj.title}')
        

