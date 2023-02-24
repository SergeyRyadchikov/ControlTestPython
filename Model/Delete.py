def delete_data():
    
    value_to_delete = input('Введите название заголовка для удаления: ')


    with open('test.csv', encoding='utf-8') as f:
        lines = f.readlines()
        
    with open('test.csv', "w", encoding='utf-8') as f:
        count = 0
        for line in lines:
            lst = line.split(',')
            if value_to_delete != lst[2]:
                f.write(line)
            else:
                count+=1
        if count != 0:
            print('Запись успешно удалена!')
        else:
            print('Такого заголовка нет!')


delete_data()