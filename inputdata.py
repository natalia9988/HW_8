from data_creat import *

def writing_person():                                       # Ввод данных
    lastname = last_name()
    name = first_name()
    tel = phone()
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(f"фамилия:{lastname} имя:{name} телефон:{tel}\n")
    data.close()

def find_data():                                            # Поиск информации в справочнике
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        phonebook = data.read().split('\n')
        temp = input('Кого ищем?: ')
        for i in phonebook:
            if temp in i:
                print(i)


def print_data():                                           # Вывод данных на экран
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')
     

def load():                                                     # Импорт данных
    new_phonebook = input("Введите ссылку: ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        with open(new_phonebook, "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
                   
                    
                    
def delete_person():  
    person_str = input('Введите данные для удаления : ')         #Удаление данных
    with open("phonebook.txt", "r", encoding="utf-8" ) as data:
        lines = data.readlines()
        with open("phonebook.txt", "w", encoding="utf-8" ) as data_1:
            for line in lines:
                if person_str not in line:
                    data_1.write(line)
                else:
                    print(line)
                    ask = input('Удалить строку? 1- да, 2- нет : ')
                    while ask not in ("1","2"):
                        print ('Ввод некорректный, введите 1 или 2 : ')
                        ask = input('Удалить строку? 1- да, 2- нет : ')
                    if ask == "2":
                        data_1.write(line)

def change_person():                                                #Изменение данных
    old_name = input('Какую запись хотите изменить?: ')
    with open("phonebook.txt", "r", encoding="utf-8" ) as data:
        lines = data.readlines()
        with open("phonebook.txt", "w", encoding="utf-8" ) as data_1:
            for line in lines:
                if  old_name not in line:
                    data_1.write(line)
                else:
                    ask = input('Что хотите изменить? 1- фамилия, 2- имя, 3 - номер телефона : ')
                    while ask not in ("1","2","3"):
                        print ('Ввод некорректный, введите 1, 2 или 3 : ')
                        ask = input('Что хотите изменить? 1- фамилия, 2- имя, 3 - номер телефона : ')
                    else:
                        print(line)
                    ask = input('Изменить эту строку? 1- да, 2- нет : ')
                    while ask not in ("1","2"):
                        print ('Ввод некорректный, введите 1 или 2 : ')
                        ask = input('Изменить эту строку? 1- да, 2- нет : ')
                    if ask == "2":
                       data_1.write(line)
                    if ask == "1":
                        new_name = input ('Введите новые данные : ')
                        line_list = line.split()
                        line_list[int(ask)] = new_name
                        data_1.write("\t".join(line_list)+'\n')
                      

