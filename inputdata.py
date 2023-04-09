from data_creat import *

def writing_person():                              # Ввод данных
    lastname = last_name()
    name = first_name()
    tel = phone()
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(f"фамилия:{lastname} имя:{name} телефон:{tel}\n")
    data.close()

def find_data():                                       # Эта ф-ция ищет информацию в справочнике
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        phonebook = data.read().split('\n')
        temp = input('Кого ищем?: ')
        for i in phonebook:
            if temp in i:
                print(i)


def print_data():                                # Вывод данных на экран
     with open('phonebook.txt', 'r', encoding='utf-8') as data:
        phonebook = data.read()
        return phonebook
     
def load():                                              # Импорт данных
    new_phonebook = input("Введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
                    data_1.write("\n")

def delete_person():  
    person_str = input('Введите данные для удаления : ')         #Удаляет данные
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

