from inputdata import*

def interface():
    print(""" 1-Ввод данных
    2- Поиск данных
    3- Вывод данных на экран
    4- Импорт данных в файл
    5- Удаление данных
    6- Изменение данных """)

    ask=int(input())
    if ask==1:
        writing_person()
    elif ask==2:
        find_data()
    elif ask==3:
        print_data
    elif ask==4:
        load()
    elif ask==5:
        delete_person()
    elif ask==6:
        change_person()
    else:
        print('Нет такой команды')