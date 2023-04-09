# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def writing_person():                                 # Ввод данных
    lastname = input("Фамилия: ")
    name = input("Имя: ")
    surname = input("Отчество: ")
    tel = input("Телефон: ")
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(f"фамилия:{lastname} имя:{name} отчество:{surname} телефон:{tel}\n")
    data.close()


def show_data():                                     # эта ф-ция показывает содержимое справочника
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        phonebook = file.read()
    return phonebook

def find_data():                                       # Эта ф-ция ищет информацию в справочнике
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        phonebook = file.read().split('\n')
        temp = input('что ищем?: ')
        for i in phonebook:
            if temp in i:
                print(i)


def delete_person():  
    person_str = input('Введите данные для удаления : ')         #Удаляет данные
    with open("phonebook.txt", "r", encoding="utf-8" ) as data:
        persons = data.readline()
        with open("phonebook.txt", "w", encoding="utf-8" ) as data_1:
            for person in persons:
                if person_str != person:
                    data_1.write(person)
                else:
                    print(person)
                    ask=input('Удалить строку? 1- да, 2- нет : ')
                    while ask not in ("1","2"):
                        print ('Ввод некорректный введите 1 или 2')
                    ask=input('Удалить строку? 1- да, 2- нет : ')
                    if ask == 2:
                        data_1.write(person)

    
def change_person():          #Изменяет данные
    old_name = input('Кого хотим переименовать?: ')
    new_name = input('Как хотим его назвать?: ')
    with open("phonebook.txt", "r", encoding="utf-8" ) as data:
        persons = data.readline()
        with open("phonebook.txt", "w", encoding="utf-8" ) as data_1:
            for person in persons:
                if  old_name != person:
                    data.write(person)
            else:
                data_1.write(new_name + "\n")

def load():                                              #Выгружает данные
    new_phonebook = input("Введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
                    data_1.write("\n")




while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-импорт: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        writing_person()
    elif mode == '3':
        delete_person()
    elif mode == '4':
       change_person()
    elif mode == '5':
        load()
    else:
        print('Нет такой команды')
    
   