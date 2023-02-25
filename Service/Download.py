import sys
sys.path.insert(0, 'Model')
from Note import Note
from Printer import Printer



class Download():

    def __init__(self, file, count):
        self.file = file
        self.count = count

    def import_count(self):
        with open(self.count, 'r', encoding='utf-8') as k:
            count = k.readlines()
        return int(count[0])

    def import_data(self):
        with open(self.file, 'r', encoding='utf-8') as k:
            lines = k.readlines()
            lst1 = []
            list_notes = []
            for each in lines:
                if each.__contains__(";"):
                    line = each.replace("\n", "")
                    lst1 = line.split(";")                    
                    list_notes.append(Note(lst1[0], lst1[1], lst1[2], lst1[3]))
                    lst1 = []
            return list_notes    
                

p = Printer
imp = Download('SystemDate\\test.csv', 'SystemDate\\save_count.txt')
p.print_list_notes(imp.import_data())
# print(imp.import_count())