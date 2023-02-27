# Приложение "Заметки"

## Информация о проекте

Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку. 

## Содержание проекта

### Модуль Model
Данный модуль соодержит один класс Note. Этот класс реализует заметку как объект, который содержит в себе 4 атрибута:
* ID
* Title (Заголовок)
* Message (Тело заметки)
* Date (Дата и время создания/изменения заметки)

### Модуль Service
Данный модуль содержит в себе 7 классов, которые реализуют функцинал приложения:

1. Add

    Данный класс реализует функционал добавления (создания) новой заметки с помощью единственной функции "add"

2. Delete

    Данный класс реализует функционал удаления заметки с помощью единственной функции "dell_note"

3. Download

    Данный класс реализует функционал загрузки данных в приложение при запуске. Содержит 2 функции:

    * import_count()
        
        Функция отвечает за загрузку ID (уникальное значение), который будет присваиваться новой заметке.

    * import_data()

        Функция отвечает за загрузку данных (заметок) созданных в ранних сессиях.

4. Edit

    Данный класс реализует функционал изменения (переименования) заголовка и изменение (дозапись) тела заметки. Содержит 3 функции:

    * enter_note()

        Функция отвечает за выбор заметки, которую будем редактировать

    * modify_title()

        Функция отвечает за редактирование заголовка

    * modify_message()

        Функция отвечает за редактирование тела заметки

5. Printer

    Данный класс реализует функционал вывода на экран. Содержит 2 функции:

    * print_note()

        Вывод на экран одной заметки со всеми параметрами (атрибутами)

    * print_list_notes()

        Вывод на экран списка всех заметом в виде -> ID | Title

6. Save

    Данный класс реализует функционал записи данных и ID в специальные системные файлы (save_count.txt и save_notes.csv). Содержит в себе единственную функцию: 

    * save_parameters() 
        
        Которая отвечает за запись в файлы.

7. Search 

    Данный класс реализует функционал поиска заметки по заголовку. Содержит в себе единственну функцию:

    * search_note()

        Которая запрашивает у пользователя данные для поиска и находит искомую заметку, в противном случае возвращает сообщение об отсутствии совпадений.


### Модуль Controller

Данный модуль является UI для взаимодействия приложения и пользователя. Содержит в себе один класс:

* Controller

    Который содержит в себе одну единственную функцию:

    * button_click()

        Которая запускает программу, управляет ей и работает до тех пор, пока пользователь не остановит работу приложения. 

### Модуль SistemDate

Это системная папка, которая содержит в себе 2 файла:
 
* save_count.txt - в файле хранится значения следующего присваиваемого ID

* save_notes.csv - импровизированная база данных, которая содержит в себе информацию обо всех сохраненных заметках в формате .csv


### Файл App.py

Точка входа в приложение. Содержит в себе вызов единственной функции контроллера, чем инициирует запуск программы.